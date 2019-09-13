d={1:'a',2:'b'}
print(d)
print(d.keys())
print(d.values())

d1=d.copy()
print(d1)
d1.clear()
print(d1)

d.setdefault(3,'c')
print(d)

d.setdefault(4)
print(d)

d.setdefault(4,'asasdf')
print(d)

d.setdefault(5,'asasdf')
print(d)

print(d.get(1))

