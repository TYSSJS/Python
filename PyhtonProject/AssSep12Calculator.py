def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def division(a,b):
    if a>b:
        return  a/b
    else:
        return a//b

print("which operation u want to perform")
print("1. add")
print("2. substract")
print("3. multiply")
print("4. divide")
operation = int(input("enter your choice"))
a = int(input("enter first number"))
b = int(input("enter first number"))

if operation == 1:
    print(add(a,b))

elif operation == 2:
    if a > b:
        print(sub(a, b))
    else:
        print("format is not correct")

elif operation == 3:
    print(mul(a, b))

else:
    print(division(a,b))
