a = int(input("enter the amount"))
print("what u want to do?")
print("1. credit")
print("2. debit")
operation = int(input("enter your choice"))
b = int(input("enter the amount"))
if operation == int(1):
    print("the new amount is: ", a+b)
else:
    print("the new amount is: ", a-b)