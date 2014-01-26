#include <sys/stat.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "checksum.h"

/* 
  Author alex
  Generated From Alexs-MacBook-Air.local
  Created At 01/10/2014 07:16:29 PM CET
*/


int main( int argc, char * argv[] ){
  int pos = 1;
  bool check = false;
  char option;


  mkdir( "/var/log/checksum", S_IRWXU | S_IRWXG | S_IRWXO );
  write_log("PROGRAM STARTED");


  if (( option = getopt( argc, argv, "hc" )) != -1){
    switch( option ){
    case 'h' :
      printf("md5sum\n");
      exit(0);	
    case 'c' : 
      check = true;
      pos +=1;
      break;
    }
  }

  if( argc < 2 ) {
    printf("Wrong number of arguments");
    exit( EXIT_FAILURE );
  }

  if( check ) {
    char * to_check = argv[pos];
    FILE * file = fopen( to_check, "r" );
    write_log("Checking checksums");
    char * buffer = malloc( 1024 );
    while( fgets( buffer, 1024, file ) != NULL ){
      char * sum = strtok( buffer, " " );
      char * name = strtok( NULL, " " );
      name = strtok( name, "\n" );
      if( strcmp( sum, compute_checksum( name ) ) != 0) {
	printf("%s FAIL.\n", name);
      }
      else {
	printf("%s OK.\n", name);
      }
    }
  }
  else {
    char * filename;
    int iter = pos;
    char * sum;
    while( iter < argc ) {
      filename = argv[iter];
      write_log("Computing checksums");
      write_log(filename);
      write_log("\n");
      sum = compute_checksum( filename );
      printf( "%s %s\n", sum, filename );
      iter ++;
    }
  }

  return EXIT_SUCCESS;
}
