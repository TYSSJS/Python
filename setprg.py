s={1,3,98,78}
s.add(34)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.add(0)
print(s)
s.pop()
print(s)
q=s.copy()
print(q)
print("set is:",q)
s.update(q)
print(s)
print(id(s))
print(id(q))
s1={1,2}
p=s1.copy()
print(s1)
print(p)
print(id(s1))
print(id(p))




