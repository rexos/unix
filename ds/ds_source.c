#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
  int statuses[2];
  int counter = 0;
  char *args[2];
  args[0] = "rm *~ &> /dev/null";
  args[1] = "rm *# &> /dev/null";

  while( counter < 2 ){
    if( fork() == 0 ){
      execlp("sh", "sh","-c", args[counter], NULL);
      printf("Failed");
      exit(EXIT_FAILURE);
    }
    else{
      pid_t id = wait(&statuses[counter]);
      counter++;
    }
  }

  if( !statuses[0] || !statuses[1] )
    printf("Cleaned\n");
  else
    printf("Already clean\n");

  return EXIT_SUCCESS;
}
