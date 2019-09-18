f=open("as1.txt","r+")
f1=open("as2.txt","w")

l=f.read().split()

for i in range(len(l)-1,-1,-1):
    s=l[i]+" "
    f1.write(s)
print("done")