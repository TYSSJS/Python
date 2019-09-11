l = [9,6,89,50.9,0.23,"done",9]
print(l.count(9))
print(l.index(50.9))
l.append(2)
print(l)
l.remove(6)
print(l)

l2 = [4,5,9,8,7,6]
l.extend(l2)
print(l)
l.insert(1,"hello")
print(l)
l2.pop(3)
print(l2)
l2.sort()
print(l2)
l.clear()
print(l)