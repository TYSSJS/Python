a = int(input("enter the first number"))
b = int(input("enter the second number"))
# print("what you want to do")
# print("1. LCM")
# print("2. HCF")
# n = int(input("enter your choice")

x = a
y = b
while (y != 0):
    temp = y
    y = x%y
    x = temp

print(y)

