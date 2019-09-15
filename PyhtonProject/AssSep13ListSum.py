l = []
s = 0
n = int(input("how many elements u want to enter"))
for i in range(n):
    element = int(input("enter the element"))
    l.append(element)
    s = s + l[i]

print(l)
print(s)