#! /bin/bash

file_path=$1

osascript <<EOF

set the_folder to (POSIX file "$file_path") as alias

tell application "Finder"
    activate
    if window 1 exists then
        set target of window 1 to the_folder
    else
        reveal the_folder
    end if
end tell

EOF