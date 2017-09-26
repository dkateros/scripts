#!/bin/sh
cd $PWD
java_file=$(find . -name $1".java")
ctf.py $java_file
