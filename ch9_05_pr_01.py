f = open('sample2.txt', 'r')
t = f.read()

if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()