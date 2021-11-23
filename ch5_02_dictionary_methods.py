myDict = {
    "fast": "In a quick manner",
    "rahul": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Rahul': 'Player'},
    1: 2
}

# Dictionary Methods

print(myDict.keys()) # Prints the key of the dictionary and it's default type is dect_keys
# print(list(myDict.keys())) # It'll convert it in list.

print(myDict.values()) # Prints values of key

print(myDict.items()) # prints the (key,value) for all contents of the dict

updateDict = {
    "Pahachan": "Friend",
    "Ankit": "Friend",
    "Deepak": "Friend",
    "rahul": "A Dancer" # this will update the already provided value 
}

myDict.update(updateDict) # updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("rahul")) # prints value associated with key "rahul"
print(myDict["rahul"]) # prints value associated with key "rahul"

# the difference between them is below...

print(myDict.get("rahul2")) # Returns None as rahul2 is not present in the dictionary
# print(myDict["rahul2"]) # Returns an error as rahul2 is not present in the dictionary

