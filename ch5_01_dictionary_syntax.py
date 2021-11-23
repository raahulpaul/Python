myDict = {
    "Fast": "In a quick manner",
    "Rahul": "A Coder",
    "Marks": [1, 2, 5],
    "Anotherdict": {'Rahul': 'Player'}
}

print(myDict['Fast'])
print(myDict['Rahul'])
# myDict['Marks'] = [45, 78] # this will change list bcoz it's mutable
print(myDict['Marks'])
print(myDict['Anotherdict'])
print(myDict['Anotherdict']['Rahul'])