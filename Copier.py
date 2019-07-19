import os
import re

# plan

# Find all the files in the directory

# If file is not a directory then create a copy with all occurances of a given word replaced with our desired word

# if we find a direcory repeat the above two steps

def replace(path):
    cwd = path + '\\'
    entries = os.listdir(path)
    files = list(map(lambda x: cwd + x, list(filter(lambda x: os.path.isfile(cwd + x), entries))))
    directories = list(filter(lambda x: not os.path.isfile(cwd + x), entries))
    
    # create the replacement files
    print("------------------------")
    print(files)
    print("------------------------")

    map(lambda x: replace(cwd + x), directories)
    
    return

replace(os.getcwd())
