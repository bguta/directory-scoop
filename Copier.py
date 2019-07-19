import os
import argparse

def replace(path):
    cwd = os.path.join(path, '')
    entries = os.listdir(cwd)
    files = list(filter(lambda x: os.path.isfile(cwd + x), entries))
    directories = list(filter(lambda x: not os.path.isfile(cwd + x), entries))
    
    # create the replacement files
    generate(files, cwd)
    return list(map(lambda x: replace(cwd+ x), directories))
    
def generate(files, cwd):
    # words to replace, make sure that each element in orignal corresponds to the same element in new
    # order is important, make sure to have the plural form first and the singular afterwards.
    orignal = ["Organizations", "organizations", "Organization", "organization"]
    new = ["Contracts", "contracts", "Contract", "contract"]
    
    mapping = {x:y for x,y in zip(orignal, new)}
    replacements = list(mapping.items())

    newCWD = cwd.replace(replacements[0][0], replacements[0][1])
    newCWD = newCWD.replace(replacements[2][0], replacements[2][1])
    
    if not os.path.exists(newCWD):
        os.makedirs(newCWD)

    # replace the title, make sure it is the capitalized one
    for arg in files:
        newFName = arg.replace(replacements[0][0], replacements[0][1])
        newFName = newFName.replace(replacements[2][0], replacements[2][1])
        # print("Replacing " + arg + " with " + newFName)
        with open(cwd + arg, "rt") as inputF:
            with open(newCWD + newFName, "wt") as outputF:
                for line in inputF:
                    for rp in replacements:
                        line = line.replace(rp[0], rp[1])
                    outputF.write(line)
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True, help="Relative Path to the head directory of the files to be replaced")
args = vars(ap.parse_args())
replace(os.getcwd() + args["dir"])
print("Done Generating the files")