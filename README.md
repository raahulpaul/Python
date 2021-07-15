# Python
letter = "Hey <|NAME|>, \n\tWelcome to Python Codes.\nZero to Hero!"
name = input("Enter your name: ")
letter = letter.replace("<|NAME|>", name)
print(letter)
