a = input("enter the string")
s=0
for i in range(0, len(a)):
    if a[i].isdigit():
        s = s + 1

print(s)