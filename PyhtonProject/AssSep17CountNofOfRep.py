# f = open("file2.txt","w")
# data = "hello i am in bangalore"
# f.write(data)
# print("done")
f = open("file2.txt","r")
w = 0
r = f.read()
print(r.count("a",0,len(r)))

