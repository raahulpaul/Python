# with - we don't need to close the file

with open('sample1.txt', 'r') as f:
    a = f.read()

with open('sample1.txt', 'w') as f:
    a = f.write("me") # this will add me in the file, actually override the file