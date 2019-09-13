s={"a","b",1,2}
print(s)
print(len(s))

print(s.add("India"))
print(s)

s1=s.copy()
print(s, "&",s1)
print(id(s),"&",id(s1))
s1.clear()
print(s1)

s.remove(2)
print(s)

s1={"good"}
s.update(s1)
print(s)
s.difference_update(s1)
print(s)
s.pop()
print(s)

