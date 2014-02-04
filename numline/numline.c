#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include "numline.h"


int main( int argc, char * argv[] ){

  mkdir( "/var/log/numline", S_IRWXU | S_IRWXG | S_IRWXO );
  write_log("PROGRAM STARTED");

  if ( argc < 2 || argc > 2 ) {
    printf("Wrong number of parameters\n");
    write_log("Wrong arguments");
    exit(1);
  }
  if ( argc == 2 && access( argv[1], R_OK ) == -1 ) {
    perror( argv[1] );
    write_log("File access denied");
    exit(1);
  }

  int fd = open(argv[1],0,O_RDONLY);
  int size = (int)(lseek(fd,0,SEEK_END));
  close(fd);
  char * filename = argv[1];
  FILE * file = fopen( filename, "r" );
  char * buffer;
  char * tmp;
  int i = 1;
  buffer = malloc( size + count_digits(i) + 2 );
  tmp = malloc( size + count_digits(i) + 2 );
  while( fgets( buffer, size, file ) ){
    sprintf( tmp, "%d) %s", i, buffer );
    printf("%s", tmp);
    buffer = malloc( size + count_digits(i) + 2 );
    tmp = malloc( size + count_digits(i) + 2 );
    i++;
  }
  return EXIT_SUCCESS;
}
