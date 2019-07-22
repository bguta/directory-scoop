# File Copier
A script to copy an existsing directory structure by replacing key words found in the files and directories
## Requirements
* python 3.x

## Setup and Run
Make sure you can run python from terminal\cmd. In the terminal or cmd, enter the following:
```
git clone "[this repo]"
cd directory-scoop
python Copier.py -p \relative\path\to\your\desired\directory
```
If you need help enter:
```
python Copier.py -h
```

## How to use?
This is a script that is designed to copy existing files within a directory and generate 
files and directories by replacing the keywords found eg. (Contract, Organization, JobRole, etc).

You can modify the script to change the mapping of words, just replace the enteries in the following two lists:
* original
* new

However, make sure that the one to one correspondence is maintained between the lists.

## Authors
* [Bereket Guta](https://github.com/bguta) - Ask me if you need help understanding/using the code
