f = open("file2.txt","r")
r =f.read()
count = 0
for i in range(len(r)):
    if r[i] == " ":
        count += 1
print(count)