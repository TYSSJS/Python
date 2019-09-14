# tuple
t = (1, 2, 3, 4, 2,"hi")
print(t)
print(t.index(2))
print(t.count(2))
print(t.__getitem__(2))
print(t.__contains__(2))

# set
s = {1, 34, 98, 1, 2, 34}
print(s)
s.add(56)
print(s)
s.add('a')
print(s)
s.pop()
print(s)
s.remove(98)
print(s)
a=s.copy()
print(a)
print(id(s))
print(id(a))
print(a.issubset(t))
print(s.difference(a))
a.clear()
print(a)
a.update(s)
print(a)
print("set is ", a)
a.discard(2)
print(a)
a.union(s)
print(a)

# dictionary

d={'d1':'tyss', 'd2':'google', 'd3':'ibm'}
print(d.keys())
print(d.values())
d1=d.copy()
print(d1)
print(id(d))
print(id(d1))
d1.clear()
print(d1)
d.setdefault('d4', 'hcl')
print(d)
# d.update(, 'iraq')
print(d)
print(d.get('d2'))


l=[1,2,3,"hi"]
l.pop(1)
print(l)
l.sort()
