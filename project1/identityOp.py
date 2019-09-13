a=[10,20]
b=a
print(a)
print(b)
print(id(a))
print(id(b))

b=[1,2,3,4]
print(b)

print(id(a))
print(id(b))

b=a
print(a)
print(b)
print(id(a))
print(id(b))

b.append(10)
print(a)
print(b)
print(id(a))
print(id(b))

print(a is b)
c=[1,2,30]
print(c is a)