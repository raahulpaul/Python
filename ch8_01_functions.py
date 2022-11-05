# marks1 = [11, 19, 69, 70, 81]
# percentage1 = (sum(marks1)/500)*100

# # We can also write like below

# marks2 = [39, 63, 69, 96, 1]
# percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3] + marks2[4])/500)*100

# print(percentage1, percentage2)

# Now with function we can write the whole code like below...

def percent(marks):
    p = (sum(marks)/500)*100
    return p

marks1 = [11, 19, 69, 70, 81]
percentage1 = percent(marks1)

# We can also write like below

marks2 = [39, 63, 69, 96, 1]
percentage2 = percent(marks2)

print(percentage1, percentage2)