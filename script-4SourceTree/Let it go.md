# Let it go

A soucetree custom action to ignore files that you don't want Git to track.

## How 2 use
Enter `Settings` -> `Custom Actions` and create a new action, perform the following config👇

 1. `Script to run`: `/usr/local/bin/git` (input the absolute path of Git)

 2. `Parameters`: `update-index --assume-unchanged $FILE`

 3. save it
 
 4. enter a repo in Sourcetree, right click on a file and choose the `Custom Actions` option, then you can see this action, just use it.
