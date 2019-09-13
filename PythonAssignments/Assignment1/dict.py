d={}
print(d)
d1=d.copy()
for i in range(0,2):
    key=input("enter key")
    val=input("enter value")
    d.setdefault(key,val)
print(d)