#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<stdio.h>
#include<string.h>
#include<sys/wait.h>
#include<unistd.h>

#define IPC_KEY 8514

int main(){


	pid_t pid = fork();
	int state;

	// parent
	if(pid != 0){
		printf("Wait for %d\n",pid);
		waitpid(pid, &state, 0);
		printf("exit %d\n", WEXITSTATUS(state));

		int mq_id;
		int rcvd = 0;
		struct{
			long type;
			int result[3];
		}mymsg;

		// set up msq
		mq_id = msgget(IPC_KEY, IPC_CREAT | 0666);
		printf("Message Identifier is %d\n", mq_id);

		// recv the msg
		rcvd = msgrcv(mq_id, &mymsg, sizeof(mymsg)-sizeof(long), 0, 0);
		printf("%d, %d, %d, (%d)\n", mymsg.result[0], mymsg.result[1],
				mymsg.result[2], rcvd);

	}
	// child
	else{
		int mq_id;
		struct{
			long type;
			int result[3];
		}mymsg;

		// set up mq
		mq_id = msgget(IPC_KEY, IPC_CREAT |0666);
		printf("Message Identifier is %d\n", mq_id);

		// send child
		memset(mymsg.result, 0, sizeof(mymsg.result));
		mymsg.type = 1;
		mymsg.result[0] = 4;
		mymsg.result[1] = 2;
		mymsg.result[2] = 1;
		msgsnd(mq_id,&mymsg, sizeof(mymsg)-sizeof(long), 0);
	}

	return 0;
}



	

