n=int(input("enter a number"))
temp=n
def fact(n):
    if n==1:
        return 1
    else:
        f=1
        while n>0:
            f=f*n
            n-=1
        return f

sum=0
while n>0:
    rem=n%10
    f=fact(rem)
    print(f)
    sum+=f
    n=int(n/10)
if temp==sum:
    print("strong number")
else:
    print("not strong number")

