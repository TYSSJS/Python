f = open("file2.txt","r")
r = f.read()
l = r.split()
print(l)
for i in range(len(l)):
    p = False
    for j in range(len(l)-1,-1,-1):
        if l[i] == l[j]:
            p = True
    if True:
        c = 1
        for j in range(len(l)):
            if l[i] == l[j]:
                break
            else:
                c += 1
    print(c)






# s = set(l)
# print("set",s)
#
# l = [1,2,3,4]
# l1 = [1,2,3,5]
# for i in range(0,len(l)):
#     if l[i] != l1[i]:
#         print(l[i])