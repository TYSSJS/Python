n=int(input("enter n"))
n1,n2=0,1
print(n1,end=" ")
print(n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
print()


