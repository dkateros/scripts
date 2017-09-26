#!/bin/sh

if [ $# -lt 1 ]
then
        echo "one argument required: the name of the java class"
        exit
fi

cd $PWD

java_file=$(find . -name $1".java")
ctf.py $java_file
