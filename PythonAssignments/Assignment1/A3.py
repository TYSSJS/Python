a=input("enter a")
b=input("enter b")
c=input("enter c")

if a>b:
    if a>c:
        print(a," is big")
    else:
        print(c," is big")
elif b>c:
    print(b," is big")
else:
    print(c," is big")