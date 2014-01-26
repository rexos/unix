#include "checksum.h"
#include <time.h>
#include <openssl/md5.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void write_log( char * line ){
  time_t now;
  FILE * logfile = fopen( "/var/log/checksum/checksum.log", "a+" );
  time( &now );
  char * original_date = ctime(&now);
  char * formatted_timestamp = (char *) malloc(40);
  strncpy(formatted_timestamp, original_date, strlen(original_date)-1);
  fprintf( logfile, "%s %s\n", formatted_timestamp, line );
  fflush( logfile );
  fclose( logfile );
}

char * compute_checksum( char * filename ) {
  FILE *file = fopen(filename, "rb");
  unsigned char digest[MD5_DIGEST_LENGTH];
  MD5_CTX mdContext;
  unsigned char data[1024];
  MD5_Init (&mdContext);
  int bytes;

  while ((bytes = fread (data, 1, 1024, file)) != 0){
    MD5_Update (&mdContext, data, bytes);
  }
  MD5_Final (digest,&mdContext);
  int i;
  char * tmp;
  char * buffer = malloc( 2 * MD5_DIGEST_LENGTH );
  for(i = 0; i < MD5_DIGEST_LENGTH; i++) {
    tmp = malloc( 2 );
    sprintf(tmp, "%02x", digest[i]);
    buffer[2*i] = tmp[0];
    buffer[2*i + 1] = tmp[1];
  }
  fclose (file);
  return buffer;
}
