a = int(input("enter first number"))
b = int(input("enter the second number"))
print("enter the operation which u want to perform")
print("1. add")
print("2. sub")
print("3. multiple")
print("4. divide")
operation = int(input())
if operation == 1:
    a += b
    print(a)

elif operation == 2:
    a -= b
    print(a)

elif operation == 3:
    a *= b
    print(a)

else:
    a/= b
    print(a)