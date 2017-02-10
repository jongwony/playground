#include<stdio.h>		// prinf
#include<stdlib.h>	// exit
#include<unistd.h>	// system call
#include<fcntl.h>		// O_RDONLY O_WRONLY
#include<string.h>	// strlen

#include<pthread.h>

// share mutex
pthread_mutex_t mutex;

void* search_word(void* arg);
int *find_word;

// share constant
int fd;
int wordpcs;
int thread_num;
char** words;

int main(int argc, char** argv){

	// mutex init
	pthread_mutex_init(&mutex, NULL);

	// argc check
	char* usage = "Usage: ./kusearch thread_number document.txt words";
	if(argc<4){
		printf("%s\n",usage);
		return 0;
	}

	// argv[1] is int?
	thread_num = atoi(argv[1]);
	if(thread_num<0){
		printf("%s\n",usage);
		return 0;
	}

	// file name
	char* document = argv[2];

	// search words
	wordpcs = argc-3;
	int i;
	words = malloc(wordpcs*sizeof(char*));
	for(i=3;i<argc;i++){
		words[i-3] = (char*)malloc(strlen(argv[i]));
		words[i-3] = argv[i];
//		printf("::%s\n",words[i-3]);
	}

	// find word size
	find_word = malloc(wordpcs*sizeof(int));
	memset(find_word,0,sizeof(wordpcs*sizeof(int)));
	
	//==========================
	
	pthread_t thr[thread_num];
	int check;
	int state;

	// file open
	fd = open(document, O_RDONLY);
	if(fd<0){
		perror("file open error");
		exit(0);
	}//sanity checked

	// separate thread index for sync
	int index[thread_num];
	for(i=0;i<thread_num;i++){
		index[i] = i;
	}

	// thread create, send start position
	for(i=0;i<thread_num;i++){
		check = pthread_create(&thr[i],NULL,search_word,(void*)&index[i]);
		if(check<0){
			perror("thread create error");
			exit(0);
		}
		//sleep(1);
	}

	// thread join
	for(i=0;i<thread_num;i++){
		pthread_join(thr[i], (void**)&state);
//		printf("thr[%d] join :: %d\n",i,state);
	}

	// close file
	close(fd);

	// result print
	printf("=========================\n");
	for(i=0;i<wordpcs;i++){
		printf("%s\t%d\n",words[i],find_word[i]);
	}
	printf("=========================\n");
	
	// output result file // write only | remove before
	fd = open("result.txt", O_WRONLY | O_TRUNC);
	if(fd<0){
		perror("file open error");
		exit(0);
	}

	// write
	for(i=0;i<wordpcs;i++){
		write(fd, words[i], strlen(words[i]));
		write(fd, "\t", 2);
		
		char buf[1];
		sprintf(buf, "%d", find_word[i]);
		write(fd, buf, sizeof(char));
		write(fd,"\n",1);
	}

	close(fd);
	
	// free memory
	free(find_word);
	free(words);

	return 0;
}

void* search_word(void* arg){
	int index=*(int*)arg;
//	printf("%lu :: %d\n",pthread_self(),index);

	// total character number
	off_t total_char = lseek(fd,0,SEEK_END);

	// matrix offset
	off_t **mat_off = NULL;
	int i=0;	// row
	int j=0; 	// column
	mat_off = malloc(wordpcs*sizeof(off_t*));
	for(i=0;i<wordpcs;i++){
		mat_off[i] = (off_t*)malloc(sizeof(off_t));
	}

	// mutex lock	(spin)
	pthread_mutex_lock(&mutex);
	
	// end position divided by index
	off_t end_pos = lseek(fd, total_char*(index+1)/thread_num,SEEK_SET);

	// start position divided by index
	// start position current!
	off_t start_pos = lseek(fd, total_char*index/thread_num, SEEK_SET);
	
	// search all words in my region
	for(i=0;i<wordpcs;i++){
		// realloc count initialize
		int c=0;

		while(lseek(fd, 0, SEEK_CUR)<end_pos){
			char buf;
			read(fd,&buf,1);

			// collecting offset
			if(buf==words[i][0]){
			// cause -1 is read 1 word before
				mat_off[i][c] = lseek(fd,0,SEEK_CUR)-1;
				
				// realloc count++
				c++;

				// realloc mat_off[i]
				mat_off[i] = realloc(mat_off[i],(c+1)*sizeof(off_t));
			}

		}//while

		// ending offset (realloc c+1 for while loop)
		mat_off[i][c] = -1;

		// debug
//		for(j=0;j<c;j++){
//			printf("i=%d, j=%d, seek=%ld\n",i,j,mat_off[i][j]);
//		}

		// rewind cursor
		lseek(fd, start_pos, SEEK_SET);
	}//for

//=================================================

		// string compare
		for(i=0;i<wordpcs;i++){
			j=0;
			while(mat_off[i][j] != -1){
				// cursor setting
				lseek(fd,mat_off[i][j], SEEK_SET);

				// read
				char word_buf[strlen(words[i])];
				read(fd,word_buf,strlen(words[i]));

				// compare each letter
				unsigned int c=0;			// strlen returns unsigned
				unsigned int count=0;	// is all letter equal?				
				for(c=0;c<strlen(words[i]);c++){
					if(words[i][c] == word_buf[c]){
						count++;
//						printf("words[%d][%d] = word_buf[%d]\n",i,c,c);
					}
//					printf("%c\t%c\n",words[i][c],word_buf[c]);
				}

				// find words!
				if(count == strlen(words[i])){
					(find_word[i])++;
				}

				// next node
				j++;
			}//while
		}//for
	

	pthread_mutex_unlock(&mutex);
	// mutex unlock

	// free offset
	for(i=0;i<wordpcs;i++){
		free(mat_off[i]);
	}
	free(mat_off);

	return (void*)index;
}
