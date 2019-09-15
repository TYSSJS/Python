d={}

n=int(input("enter number of entries"))
for i in range(n):
    key=input("enter key")
    val=input("enter value")
    d.setdefault(key,val)
print(d)
k=input("enter a key to be searched")

if d.get(k):
    print("present")
else:
    print("not present")
