#include<stdio.h>	// printf
#include<stdlib.h>	// exit
#include<unistd.h>	// system call
#include<fcntl.h>	// O_RDONLY O_WRONLY
#include<string.h>	// strlen

#include<sys/wait.h>	// wait
// IPC include
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>

#define IPC_KEY 65536

pid_t multiple_fork(pid_t parentpid, pid_t* childpid,
		int* index, int process_num);

int main(int argc, char **argv){

	// argc check
	char* usage = "Usage: ./kusearch process_number document.txt words";
	if(argc<4){
		printf("%s\n",usage);
		return 0;
	}

	// argv[1] is Int?
	int process_num = atoi(argv[1]);
	if(process_num<0){
		printf("%s\n", usage);
		return 0;
	}
	
	// get this process pid
	pid_t parentpid = getpid();
//	printf("parentpid : %d\n",parentpid);

	// child process array for wait process
	pid_t childpid[process_num];
	
	// file name 
	char* document = argv[2];

	// search words
	char **words = NULL;
	int wordpcs = argc-3;
	int i;
	words = malloc(wordpcs*sizeof(char*));
	for(i=3;i<argc;i++){
		words[i-3] = (char*)malloc(strlen(argv[i]));
		words[i-3] = argv[i];
//		printf("::%s\n",words[i-3]);
	}

	//===========================

	// fork distribution
	// pid returns real process id
	int index = 0;
	pid_t pid = multiple_fork(parentpid, childpid, &index, process_num);
	
	if(pid == parentpid){
//		printf("\nthis is parent %d, %d\n",pid, getpid());

		// wait child process
		int state;
		for(i=0;i<process_num;i++){
			waitpid(childpid[i], &state, 0);
//			printf("process(%d) exitcode %d\n",childpid[i],
//					WEXITSTATUS(state));
		}

		//-------------------------------
		// message queue
		int mq_id;
		struct{
			long type;
			int result[wordpcs];
		}ret;

		// receive array
		int recv_array[wordpcs];
		memset(recv_array, 0, sizeof(recv_array));

		// setup message queue
		mq_id = msgget(IPC_KEY, IPC_CREAT | 0666);

		// parent process receive the message
		for(i=0;i<process_num;i++){
			// receive type i+1 message
			msgrcv(mq_id, &ret, sizeof(ret)-sizeof(long),i+1,0);

			// debug
//			printf("=======\n");
//			printf("type:%ld\n",ret.type);

			int j=0;
			for(j=0;j<wordpcs;j++){
//				printf("result[%d] = %d\n",j,ret.result[j]);
				recv_array[j] += ret.result[j];
			}
//			printf("=======\n");
		}

/*		// recv_array debug
		for(i=0;i<wordpcs;i++){
			printf("recv_array[%d] = %d\n",i,recv_array[i]);
		}
*/
		// output result file		// write only | remove before
		int fd;
		fd = open("result.txt", O_WRONLY | O_TRUNC);
		if(fd<0){
			perror("file open error");
			exit(0);
		}

		// write
		for(i=0;i<wordpcs;i++){
			write(fd, words[i], strlen(words[i]));
			write(fd, "\t", 2);
			printf("%s\t",words[i]);
			
			char buf[1];
			sprintf(buf, "%d", recv_array[i]);
			write(fd, buf, sizeof(char));
			write(fd, "\n", 1);
			printf("%d\n",recv_array[i]);
		}

		close(fd);


	}
	// each child process
	else{
//		printf("\nthis is child %d, %d\n", pid, getpid());
			
		// file open
		int fd;
		fd = open(document, O_RDONLY);
		if(fd<0){				
			perror("file open error");
			exit(0);
		}	
		// sanity checked

		// total character number
		off_t total_char;
		total_char = lseek(fd, 0, SEEK_END);
//		printf("pointer end: %ld\n", total_char);

		// position divide, index: 1, 2, 3 ... process_num
		off_t cur_pos;
		cur_pos = lseek(fd, total_char*(index-1)/process_num,SEEK_SET);
//		printf("pointer cursor: %ld\n", cur_pos);

		//int i=0;					// row
		int j=0;					// column
		off_t **mat_off = NULL;		// matrix offset

		//initialize
		mat_off = malloc(wordpcs*sizeof(off_t*));
		for(i=0;i<wordpcs;i++){
			mat_off[i] = (off_t*)malloc(sizeof(off_t));
		}

		// search all words
		for(i=0;i<wordpcs;i++){
//			printf("----------first letter: %c\n",words[i][0]);

			int c=0;		// realloc count initialize
			while(lseek(fd,0,SEEK_CUR)<total_char*index/process_num){
				char buf;
				read(fd,&buf,1);
//				printf("buf:%c\n",buf);

				// collecting offset
				if(buf==words[i][0]){
					// cause -1 is read 1 word before
					mat_off[i][c] = lseek(fd,0,SEEK_CUR)-1;

					// realloc count++
					c++;
					
					// realloc mat_off[i]
					mat_off[i] = realloc(mat_off[i], (c+1)*sizeof(off_t));
				}
			}
			// ending offset (realloc c+1 for while loop)
			mat_off[i][c] = -1;
			
/*			
			// debug
			for(j=0;j<c;j++){
				printf("i=%d,j=%d,seek=%ld\n",i,j,mat_off[i][j]);
			}
*/			
			
			// rewind cursor
			lseek(fd, cur_pos, SEEK_SET);
//			printf("cur_pos=%ld\n", lseek(fd,cur_pos,SEEK_SET));
		}	// for

		// result array
		int find_word[wordpcs];
		memset(find_word,0,sizeof(find_word));

		// string compare
		for(i=0;i<wordpcs;i++){
			j=0;
			while(mat_off[i][j] != -1){
//				printf("mat_off[%d][%d] = %ld\n",i,j,mat_off[i][j]);

				// infinite loop debug
//				 sleep(1);
				
				// cursor setting
				lseek(fd,mat_off[i][j],SEEK_SET);
//				printf("cur_pos = %ld\n", lseek(fd,mat_off[i][j],SEEK_SET));
				
				// read
				char word_buf[strlen(words[i])];
				read(fd,word_buf,strlen(words[i]));

				// compare each letter
				unsigned int c=0;		// strlen returns unsigned
				unsigned int count = 0;	// is all letter equal?
				for(c=0;c<strlen(words[i]);c++){
					if(words[i][c] == word_buf[c]){
						count++;
//						printf("words[%d][%d] = word_buf[%d]\n",i,c,c);
					}
//						printf("%c\t%c\n",words[i][c],word_buf[c]);
				}

				// find words!
				if(count == strlen(words[i])){
					(find_word[i])++;
				}

				// next node
				j++;
			}//while
		}//for

		// file close
		close(fd);

		// free offset
		for(i=0;i<wordpcs;i++){
			free(mat_off[i]);			
		}
		free(mat_off);

		// debug
/*		printf("--------------------------\n");
		for(i=0;i<wordpcs;i++){
			printf("find_word[%d] = %d\n",i,find_word[i]);
		}
		printf("--------------------------\n");

		// ----------------------------------------
*/
		// IPC send
		int mq_id;
		struct{
			long type;
			int result[wordpcs];
		}ret;

		// setup the message queue
		mq_id = msgget(IPC_KEY, IPC_CREAT | 0666);
		
		// send a message
		memset(ret.result, 0, sizeof(ret));
		ret.type = index;
//		printf("send type = %ld\n",ret.type);
		for(i=0;i<wordpcs;i++){
			ret.result[i] = find_word[i];
//			printf("send result[%d] = %d\n",i,find_word[i]);
		}

		msgsnd(mq_id, &ret, sizeof(ret)-sizeof(long),0);
//		printf("message send\n");

//		sleep(1);

	}	// else

	// free memory
	free(words);
	return 0;
}

// recursive function
pid_t multiple_fork(pid_t parentpid, pid_t* childpid,
		int* index, int process_num){

	// recursive end
	(*index)++;
	if((*index)>process_num){
		return getpid();
	}

	pid_t pid = getpid();

	// only parent pid is fork available
	if(parentpid == pid){
		//printf("parent : %d, pid = %d\n",parentpid, pid);
		// debug
//		sleep(1);
		pid = fork();
	}

	if(pid != 0){
		// child pid save for waitpid
		childpid[(*index)-1] = pid;

		// pid initialize
		pid = parentpid;

		// parent process just recursive fork
		pid = multiple_fork(parentpid, childpid, index, process_num);

		return getpid();
	}
	// child process, pid is 0 or child getpid()
	else{
		return getpid();
	}
}
