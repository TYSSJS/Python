# n=int(input("enter n"))
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()

n=int(input("enter n"))
for i in range(n):
    num=1
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()