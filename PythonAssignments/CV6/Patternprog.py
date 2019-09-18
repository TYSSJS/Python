# n=int(input("enter n"))
# for i in range(n):
#     num=1
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

# n=int(input("enter n"))
# num=1
# for i in range(1,n+1):
#
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()
#

# n=int(input("enter n"))
# num = 65
# for i in range(1,n+1):
#
#     ch=chr(num)
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         num+=1
#     print()

def patt(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print()
patt(5)

