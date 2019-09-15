print("what do u want?")
print("1. largest even number")
print("2. largest odd number")
a = int(input("enter your choice"))
i = int(input("enter upto what range u want to search"))
l=[]
l1=[]
for num in range(0,i+1):
    if a == 1:
        if num % 2 == 0:
            l.append(num)

    else:
        if num % 2 != 0:
            l1.append(num)

if a == 1:
    print(l)
    print("largest even number is: ", l[-1])
else:
    print(l1)
    print("largest odd number is: ", l1[-1])




