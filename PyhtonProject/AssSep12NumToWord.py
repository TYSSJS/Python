lst = []
n = int(input("enter number of element: "))
print("print number. But should be  between 0 to 9 ")
for i in range(0,n):
    element = int(input())
    lst.append(element)

print(lst)

for i in range(0,n):
    if lst[i] == 0:
        print("zero")

    elif lst[i] == 1:
        print("one")

    elif lst[i] == 2:
        print("two")

    elif lst[i] == 3:
        print("three")

    elif lst[i] == 4:
        print("four")

    elif lst[i] == 5:
        print("five")

    elif lst[i] == 6:
        print("six")

    elif lst[i] == 7:
        print("seven")

    elif lst[i] == 8:
        print("eight")

    elif lst[i] == 9:
        print("nine")

    else:
        print("format not correct")
