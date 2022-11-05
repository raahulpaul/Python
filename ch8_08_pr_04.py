# sum(n) = 1 + 2 + 3 + 4.......n-1 + n
# sum(n) = sum(n-1) + n

def sum(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n + sum(n-1)

n = 5
print(sum(n))