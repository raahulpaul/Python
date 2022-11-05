with open("sample6.txt", 'r') as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, Python is present")

else:
    print("No, Python is not present")