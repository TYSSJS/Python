#swap two numbers
a=int(input("enter a"))
b=int(input("enter b"))

print("the numbers before swap")
print("a=",a," b=",b)
a=a+b
b=a-b
a=a-b

print("the numbers after swap")
print("a=",a," b=",b)
