#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(void){
	pid_t pid;

	printf("fork before\n");
	pid = fork();

	// child process
	if(pid==0){
		printf("return pid = %d, getpid = %d",pid,getpid());
	}
	else{
		printf("return pid = %d, getpid = %d",pid,getpid());
	}

	printf("\n");
	
	return 0;

}
