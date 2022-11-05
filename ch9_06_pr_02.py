def game():
    return 555

score = game()
with open("sample3.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr=='':
    with open("sample3.txt", "w") as f:
        f.write(str(score)) 

elif int(hiscoreStr)<score or hiscoreStr=='':
    with open("sample3.txt", "w") as f:
        f.write(str(score))