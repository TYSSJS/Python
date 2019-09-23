f = open("file2.txt","r+")
r = f.read()
l = r.split()
for i in range(len(l)-1,-1,-1):
    s = l[i]+" "
    f.write(s)
print("done")
