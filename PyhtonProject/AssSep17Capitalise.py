f = open("file2.txt","r+")
r = f.read()
t = r.title()
print(t)
f1 = open("fil.txt","w")
f1.write(t)
print("done")