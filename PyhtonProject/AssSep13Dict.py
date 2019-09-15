n = int(input("how many key value u want to enter"))
d={}
for i in range(0,n):
    k = input("enter the key")
    v = input("enter the value")
    d.setdefault(k,v)

print(d)