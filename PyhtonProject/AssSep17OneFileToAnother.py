f = open("fil1.txt","r")
r=f
f1 = open("duplicate","w")
for i in range(0,1):
    f1.writelines(r)
print("done")