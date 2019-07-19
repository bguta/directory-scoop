import os
import argparse
    
def generate(files, cwd):
    #------------------------------------------------------------------------------------------#
    # words to replace, make sure that each element in orignal corresponds to the same element in new
    # order is important, make sure to have the plural form first and the singular afterwards.
    orignal = ["Organizations", "organizations", "Organization", "organization"] # You can modify these entries
    new     = ["Contracts", "contracts", "Contract", "contract"] # You can modify these entries
    #------------------------------------------------------------------------------------------#
    
    mapping = {x:y for x,y in zip(orignal, new)}
    replacements = list(mapping.items())

    newCWD = cwd.replace(replacements[0][0], replacements[0][1])
    newCWD = newCWD.replace(replacements[2][0], replacements[2][1])
    
    if not os.path.exists(newCWD):
        os.makedirs(newCWD)

    def reproduce(arg):
        # avoid replacing these two files
        if not (arg == 'Copier.py' or arg == 'README.md'):
            # replace the title, make sure it is the capitalized one
            newFName = arg.replace(replacements[0][0], replacements[0][1])
            newFName = newFName.replace(replacements[2][0], replacements[2][1])

            with open(cwd + arg, "rt") as inputF:
                with open(newCWD + newFName, "wt") as outputF:
                    for line in inputF:
                        for rp in replacements:
                            line = line.replace(rp[0], rp[1])
                        outputF.write(line)

    return list(map(lambda x: reproduce(x), files))

def replace(path):
    cwd = os.path.join(path, '')
    entries = os.listdir(cwd)
    files = list(filter(lambda x: os.path.isfile(cwd + x), entries))
    directories = list(filter(lambda x: not os.path.isfile(cwd + x), entries))
    
    # create the replacement files
    generate(files, cwd)
    return list(map(lambda x: replace(cwd+ x), directories))
    
#--------------------------------#
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="Relative Path to the head directory of the files to be replaced (eg. ..\D1\D2 )")
args = vars(ap.parse_args())

replace(os.path.join(os.getcwd(), args["path"]))
print("Done Generating the files")
#--------------------------------#