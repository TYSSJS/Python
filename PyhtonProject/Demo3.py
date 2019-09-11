from builtins import print

l = [10, 20, 13.25, "hi", 10]
print(l.count(10))
print(l.index("hi"))
print(l.remove(10))
print(l)
l1 = [12,13.56, 125799]
print(l.extend(l1))
print(l)
print(l.insert(1, "hello"))
print(l)
print(l.pop(2))
print(l)

g = [1,2,3,4,8,6,5,7]
g.sort()
print(g)
g.append("hi")
print(g)

