s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # this will give 2 because of equal values in set.
print(s)

t = {}
print(type(t))