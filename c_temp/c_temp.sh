#!/bin/sh

# constants
TIMESTAMP=$(date +"%x %r %Z")
AUTHOR=$(whoami)
HOSTNAME=$(hostname)

# functions
function get_host
{
    echo "Created At $TIMESTAMP"
}

function get_author
{
    echo "Author $AUTHOR"
}

function get_timestamp
{
    echo "Generated From $(HOSTNAME)"
}

# 'here document' redirected (append) to cat command
cat <<_END_
#include <stdio.h>
#include <stdlib.h>

/* 
  $(get_author)
  $(get_timestamp)
  $(get_host)
*/

int main(){

  //Implement program here

  return 0;
}
_END_
