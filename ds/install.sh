#! /bin/bash
name=""
URL="https://raw.github.com/rexos/unix/master/ds/ds_source.c"
sourcename="source.c"


if [ -e /usr/bin/curl ]; then
    curl $URL > $sourcename
else
    which wget
    if [ $? == 0 ]; then
	wget $URL > $sourcename
    else
	echo "No tools needed to retrieve web content found ... "
	exit
    fi
fi

if [ -f source.c ] &&
    [ -e /usr/bin/gcc ]; then
  
    echo "command name : "
    read name
    gcc source.c -o $name
    sudo cp ./$name /bin/$name 
    if [ $? == 0 ]; then
	echo "$name successfully installed"
    else
	echo "error while installing $name"
    fi
    echo "cleaning ..."
    rm ./$name
    rm ./source.c
else
    echo "some requirements are missing ... retry"
fi