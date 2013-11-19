#! /bin/bash
name=""

if [ -f ds_source.c ] &&
    [ -e /usr/bin/gcc ]; then
    
    echo "command name : "
    read name
    gcc ds_source.c -o $name
    sudo cp ./$name /bin/$name
    rm ./ds
    if [ $? == 0 ]; then
	echo "$name successfully installed"
    else
	echo "error while installing $name"
    fi
fi