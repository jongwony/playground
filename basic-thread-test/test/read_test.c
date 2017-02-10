#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>

int main(void){
	int fd;

	// lseek의 포인터
	off_t p;

	// file open and sanity check
	fd = open("./test.txt",O_RDONLY);
	if(fd<0){
		perror("file open error");
		exit(0);
	}

	p = lseek(fd, 0, SEEK_END);
	printf("pointer end: %ld\n",p);

	close(fd);
	return 0;
}
