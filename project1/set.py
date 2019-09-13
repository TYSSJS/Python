s={'a',11,12,12}
print(s)

print(s.add("sara"))
print(s)
s1=s.copy()
print(s1)
s1.clear()
print(s1)

# s.pop()
# print(s)

print(s.add('India'))
print(s)

s.remove('a')
print(s)
print(s)

s2={'a',11,12,3,4}
print(s2)
print(s.difference(s2))

s.update(s2)
print("s: ", s)