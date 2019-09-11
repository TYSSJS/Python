l=[1,2,3,4]
l1=l.copy()
print(l1)

print(l1.count(4))
l1.insert(1,4)
print(l1)
l1.remove(4)
print(l1)

l2=['a','b']
l1.extend(l2)
print(l1)
print(l1.index('a'))
l1.insert(0,1)
print(l1)

print(l1.index(1,1))
l3=l1.copy()
print(l3)

l3.clear()
print(l3)

print(l1.count(1))
print(l1.reverse())

print(l1)
l1.reverse()
print(l1)

l1.pop(0)
print(l1)

print(len(l1))


