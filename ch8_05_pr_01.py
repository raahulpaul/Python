def greatest(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

print(greatest(num1, num2, num3))



# We can also write as below...

def maximum(int1, int2, int3):
    if(int1>int2):
        if(int1>int3):
            return int1
        else:
            return int3
    else:
        if(int2>int3):
            return int2
        else:
            return int3

m = maximum(13, 55, 22)
print("The value of the maximum is "+ str(m))