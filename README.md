# File Copier

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

You can modify the script to change the mapping of words, just replace the following two lists:
* original
* new

However, make sure that the one to one correspondence is maintained between the lists
