import random

def gamewin(comp, you):
    if comp == you:
        return None
    
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True



print("Comp already choose from: Snake(s), Water(w), Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"

elif randNo == 2:
    comp = "w"

elif randNo == 3:
    comp = "g"

you = input("Your turn choose from: Snake(s), Water(w), Gun(g)? ")

print(f"comp choose {comp}")
print(f"You choose {you}")

a = gamewin(comp, you)

if a == True:
    print("You Win!")

elif a == False:
    print("You Loose!")

elif a == None:
    print("Game is Tie!")