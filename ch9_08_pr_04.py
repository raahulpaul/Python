with open("sample4.txt", 'r') as f:
    content = f.read()

content = content.replace("donkey", "#####")

with open("sample4.txt", 'w') as f:
    f.write(content)