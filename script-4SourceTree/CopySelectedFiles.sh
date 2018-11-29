#!/bin/bash
# copy selected files to target dir in SourceTree

# !!! target dir U need to set !!!
$target_dir="your target directory(absolute path)"

repo_path=$1
flag=0
for i in "$@"; do
	flag=`expr $flag + 1`
	if [[ $flag != 1 ]]; then
 		cp ${repo_path}"/"$i $target_dir
	fi
done
