d={}

n=int(input("enter number of emp"))

for i in range(n):
    name=input("name:")
    id=int(input("id"))
    ph=int(input("phone no"))
    l=[name,ph]
    d.setdefault(id,l)
print(d)