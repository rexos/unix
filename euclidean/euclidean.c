#include <stdio.h>
#include <stdlib.h>

/* 
  Author alex
  Generated From Alexs-MacBook-Air.local
  Created At 03/20/14 05:20:57 PM CET
*/

int gcd( int a, int b ){
  int r;
  while (1){
    r = a % b;
    if( r == 0 ){
      return b;
    }
    a = b;
    b = r;
  }
}

int main(){

  printf("%d\n", gcd(1547,560));

  return 0;
}
