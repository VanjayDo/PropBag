#!/bin/bash

ParameterNum=$#

if [[ $ParameterNum > 3 ]]; then
	DATE=$1
	TIME=$2
	FILE="$3"
	COMMENT="$4"
	if [[ $ParameterNum == 5 ]]; then
		TimeZone=$5
	else
		TimeZone=08:00 #here take Beijing Time as an example
	fi

	GIT_COMMITTER_DATE=${DATE}T${TIME}+${TimeZone}
	GIT_AUTHOR_DATE=$GIT_COMMITTER_DATE

	git add "$FILE"
	GIT_COMMITTER_DATE=$GIT_COMMITTER_DATE GIT_AUTHOR_DATE=$GIT_AUTHOR_DATE git commit -m "$COMMENT"

else
echo """
U must input at least 4 parameters, followed by:
  1. Date like 2019-01-01;
  2. Time like 23:35:02;
  3. Path of files enclosed by quotes like "./readme.md"
  4. Comment like "docs\(readme.md\):add readme file\;"
 [5].Time zone, like 08:00, which is Beijing time zone. This para is optional.
"""
fi
