#! /bin/bash
name=""

if [ -e /usr/bin/curl ]; then
    curl https://raw.github.com/rexos/unix/master/ds/ds_source.c > source.c
else
    wget https://raw.github.com/rexos/unix/master/ds/ds_source.c > source.c
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
fi