n=int(input("enter size of the list"))
l=[]
for i in range(n):
    num=int(input("enter list element"))
    l.append(num)
print(l)

def big(l):
    big=l[0]
    for i in range(1,len(l)):
        if l[i]>big:
            big=l[i]
    print(big)
big(l)