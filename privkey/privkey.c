#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/* 
  Author alex
  Generated From Alexs-MacBook-Air.local
  Created At 03/20/14 05:20:57 PM CET
*/

int prime(int n){
  // trivial division algorithm to determine number primality
  // to be improved
  for( int i = 2; i*i <= n; i++ ){
    if( n % i == 0 )
      return false;
  }
  return true;
}

int compute_totient( int p, int q ){
  if( prime(p) && prime(q) )
    return (p-1)*(q-1);
  return -1;
}

int gcd( int a, int b, int * d ){
  // implements the extended euclidean algorithm to compute
  // the modular inverse of the pubk with respect for
  // the totient of n
  int s0 = 0;
  int s1 = 1;
  int s;
  int q;
  int r;
  while (1){
    r = a % b;
    if( r == 0 ){
      *d = s;
      return b;
    }
    q = a/b;
    s =  s0 - q*s1;
    s0 = s1;
    s1 = s;
    a = b;
    b = r;
  }
}

int main(){
  int d = 0;
  int p,q,pubk;
  printf("Two prime numbers p and q :\n");
  scanf("%d", &p);
  scanf("%d", &q);
  printf("Choose a public key:\n");
  scanf("%d", &pubk);
  int phi = compute_totient( p, q );
  if( phi == -1 ){
    printf("p or q or both are not prime, retry");
    exit(-1);
  }
  int g = gcd(phi,pubk, &d);
  if ( g == 1 ){
    printf("The private key is:\n");
    if( d < 0 ){
      printf("%d\n", phi+d);
    }
    else{
      printf("%d\n", d%phi);
    }
  }
  else{
    printf("No modular inverse exists\n");
  }
  return 0;
}
