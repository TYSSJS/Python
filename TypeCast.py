l=[12,10,45,55,10,"hi"]
print(l.count(10))
print(l.index('hi'))
print(l.remove(10))
# first occurrence will remove if there are duplicates
print(l)

l1=[19,12.354,1,5,9]
l.extend(l1)
print(l)
l.insert(1,'hello')
print(l)
l.pop(0)
print(l)
print(l.clear())
a=(l1.copy())
print("copied value",a)
a.sort()
# sort will work for only homogeneous not for hetrogenous
print(a)
l1.append('hi')
print(l1)


