a = 12
b = 23
def add_Number(a1, b1):
    print(a1 + b1)
add_Number(a, b)

for i in range(10):
    print(i, end=" ")
print(" ")
l = [12, 23, 34, 2, 3, 4]
for i in l:
    print(i)
    print(l[2])
print(" ")
for i in range(1, len(l)):
    print(l[i], end=" ")
print(" ")
for i in range(l.index(23), len(l)):
    print(l[i], end=" ")