a = 45

# if-elif-else ladder in python. it will print the first value which is true and ignores everything.
if(a>3):
    print("The value of a is greater than 3")
elif(a>13):
    print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

# Multiple if statements

if(a>3):
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")

if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")


# Quiz

age = int(input("Enter your age: "))

if age>=18:
    print("Yes")
else:
    print("No")