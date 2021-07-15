# Concatenating two strings
# greeting = "Good Morning, "
# name = input("Enter your name: ")
# c = greeting + name
# print(c)

# Slicing
name = "Rahul"
# print(name[4])

# name[3] = "d" --> Does not work because we can't change string.

print(name[0:3]) # --> will print 0 to 2
print(name[:4]) # --> Will automatically take the lowest index in string
print(name[0:]) # --> Will automatically take the highest index in string

print(name[-4:-1]) # --> -1 means the last index of string and count it further in reverse.

print(name[1:4:2]) # --> the last value i.e. 2 is used to skip every second number.

a = "Rahul is a developer"
print(a[0::3])