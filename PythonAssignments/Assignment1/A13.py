#reverse a number
n=int(input("enter a number"))
print("the number is", n)
rev=0
while n>0:
    print("hi")
    rem=n%10
    rev=rev*10+rem
    n=int(n/10)

print(rev)