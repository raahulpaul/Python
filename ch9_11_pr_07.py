content = True
i = 1

with open("sample6.txt", 'r') as f:
    while content:
        content = f.readline()

        if "python" in content.lower():
            print(content)
            print(f"Yes, Python is present on line number {i}")
        i += 1
    