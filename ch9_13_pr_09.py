with open("sample4.txt", 'r') as f:
    content1 = f.read()

with open("sample7.txt", 'r') as f:
    content2 = f.read()

if content1 == content2:
    print("Both files are identical")
else:
    print("Both files are not identical")