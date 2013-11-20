#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>
#include <unistd.h>

int main(){
  int statuses[2];
  int counter = 0;
  char *args[2];
  const char *dest = " &> /dev/null";
  args[0] = "rm *~";
  args[1] = "rm *#";
  char *cmd = malloc( strlen(args[0]) + strlen(dest) );

  while( counter < 2 ){
    if( fork() == 0 ){
      strncpy(cmd, args[counter], strlen(args[counter]));
      execlp("sh", "sh","-c", strncat( cmd, dest, strlen(dest) ), NULL);
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
