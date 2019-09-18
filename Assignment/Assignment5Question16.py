#16. create one file perform addition,mul,subs,division and that method in one more file using import.
def calculator():
    sum=lambda a,b :a+b
    print(sum(1,2))
    print(sum(2,3))

    subs=lambda a,b: a-b
    print(subs(4,2))

    subs=lambda a,b: a*b
    print(subs(4,2))

    subs=lambda a,b: a/b
    print(subs(4,2))

calculator()