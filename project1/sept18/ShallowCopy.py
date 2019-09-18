#shallow copy
l=[1,2,3,4]
l1=l
l.append(5)
print(l)
print(l1)
print(id(l))
print(id(l1))

#deep copy
l2=l.copy()
print(id(l))
print(id(l2))
l.append(10)
print(l)
print(l2)
