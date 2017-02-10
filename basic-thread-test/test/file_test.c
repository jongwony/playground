#include<stdio.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include<stdlib.h>

int main(void){
	int fd, i;
	char *buff = "My name is Jongwon Computer and Mathematics Major.";
 
	fd = open("test.txt", O_WRONLY | O_CREAT, 0644);
	if(fd<0){
	 	perror("file open error");
		exit(0);
	}

	write(fd, "bbbbbbb", 8);

	for(i=0;i<5;i++){
	  	write(fd, buff, strlen(buff));
	}
	write(fd, "\n",2);
	close(fd);

	return 0;

}
