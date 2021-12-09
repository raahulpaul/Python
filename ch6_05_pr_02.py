s1 = int(input("Enter subject-1 marks: "))
s2 = int(input("Enter subject-2 marks: "))
s3 = int(input("Enter subject-3 marks: "))

if s1<33 or s2<33 or s3<33:
    print("You are fail")

elif (s1+s2+s3)/3 < 40:
    print("You are fail")

else:
    print("You are pass")