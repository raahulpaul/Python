myDict = {
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item"
}

print("options are ", myDict.keys())
a = input("Enter the hindi word: ")
# print("The meaning of your word is: ", myDict[a])

# this below line will not give any error while the given word is not present in dictionary..
print("The meaning of your word is: ", myDict.get(a))
