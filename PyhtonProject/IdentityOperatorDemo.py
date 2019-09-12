a = [1,2.3]
print("a", a)
print("id a", id(a))
b = a
print("b", b)
print("id b",id(b))
b = [9,6]
c = b.append(12)
print("c", c)
print("id c",id(c))
print("new b", b)
print("id a",id(a))
print("a",a)
print("b",b)
print("id b", id(b))
print(a is b)
print(a is not b)