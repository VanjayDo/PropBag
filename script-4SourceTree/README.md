# Scripts for SourceTree

Scripts in this directory are written for SourceTree. They can be used to set `Costume Actions` in `Actions` to realize functions not supplied by SourceTree. 

## Copy Selected Files
This script is used to quickly backup the selected files to another specified directory.

Please set `$target_dir` as the directory you want to move files to(absolute path)

## Let it go
Use the command `git update-index --assume-unchanged` to ignore files that you don't want Git to track.

Read the file `Let it go.md` and follow steps listed, quite simple.

## Reveal In Finder
There is no shortcut to reveal the selected file in the Finder, so this script is created for this purpose.

## Attention
You should give scripts executable status, like chmod 0755 file. Or it may be report an error like `launch path not accessible` when runing in Unix-like OS.