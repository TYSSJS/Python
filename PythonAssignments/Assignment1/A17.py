a=int(input("enter a"))
b=int(input("enter b"))
op=input("enter (+,-,*,/,%,)")

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
elif op=='%':
    print(a%b)
else:
    print("the entered symbol is not an arithmatic operator :) enter the valid operator")
