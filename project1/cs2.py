# nested if

a=input("enter a")
b=input("enter b")
c=input("enter c")

if a<b:
    if a<c:
        print(a," is small")
    else:
        print(c," is small")
elif b<c:
    print(b," is small")
else:
    print(c," is small")

