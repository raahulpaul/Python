a = {1, 3, 4, 5, 1}
print(type(a))
print(a) # it'll not print repetitive elements

# EMPTY SET

# Important: this syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))

# METHODS IN SETS

b.add(4) # it'll add elements in empty set
b.add(5)
# b.add([4, 5, 6]) # gives error because we can't add list in set
b.add((4, 5, 6)) # we can add tuples in list
# b.add({4:5}) # can't add disctionary in sets
print(b)

# LENTH OF SET
print(len(b)) # prints the length of set

# REMOVAL OF SET
b.remove(5) # removes 5 from sets
print(b)

print(b.pop()) # removes an element and return...