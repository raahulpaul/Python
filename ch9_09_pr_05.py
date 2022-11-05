words = ["donkey", "stupid", "idiot"]

with open("sample5.txt", 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#####")

    with open("sample5.txt", 'w') as f:
        f.write(content)