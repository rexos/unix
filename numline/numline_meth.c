#include "numline.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void write_log( char * line ){
  time_t now;
  FILE * logfile = fopen( "/var/log/numline/numline.log", "a+" );
  time( &now );
  char * original_date = ctime(&now);
  char * formatted_timestamp = (char *) malloc(40);
  strncpy(formatted_timestamp, original_date, strlen(original_date)-1);
  fprintf( logfile, "%s %s\n", formatted_timestamp, line );
  fflush( logfile );
  fclose( logfile );
}

int count_digits( int number ){
  int ret = 0;
  while( number != 0 ){
    number = number / 10;
    ret ++;
  }
  return ret;
}
