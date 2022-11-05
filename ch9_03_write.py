# ****Write****

# f = open('sample1.txt', 'w') # this will override the whole file, if its already existing otherwise create a new file and write
# f.write("I am writing") # This can be executed multiple times
# f.close()



# ****Append****

f = open('sample1.txt', 'a') # This will add new text to the file and doesn't override
f.write("I am adding text") # This can be executed multiple times
f.close()