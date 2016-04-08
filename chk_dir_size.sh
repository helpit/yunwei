#!/bin/bash
shopt -s -o nounset

DIR=$(1:?'请提供想检查的路径，如：/var')

if [[ ! $DIR == /* ]]; then
    DIR=/$DIR
fi

declare -i size SIZE 

SIZE=5000

while read size dir 
do 
    if [ $size -gt $SIZE ]; then
        echo -e "$size\t\t$dir"
    fi

done < <(find $DIR -mindepth 1 -type d -exec du -sm () \;)


