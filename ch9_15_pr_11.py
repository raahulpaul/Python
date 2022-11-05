import os

oldfile = "sample9.txt"
newfile = "sample_renamed_by_python.txt"

with open(oldfile, 'r') as f:
    content = f.read()

with open(newfile, 'w') as f:
    f.write(content)

os.remove(oldfile)