l=[1,2.2,'hi']
print(l)
print(l.insert(0,'good'))
print(l)

l1=[10,10,20]
print(l.extend(l1))
print(l)
print(l.count(10))

l2=l.copy()
#print(l2)

print(l.index('hi'))
print(l.remove(10))
print(l)
l.reverse()
print(l)

print(l.pop(0))
print(l)

n=l.__len__()
print(n)
print(len(l))
# l3=l.__add__(l2)
# print(l3)
a1=[1,2]

(a1.append(3))
print(a1)
(a1.append('hi'))
print(a1)
