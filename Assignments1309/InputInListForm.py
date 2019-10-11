l1, total = [], 0
for i in range(int(input("Enter the number of elements you want in the list: "))):
    num = int(input("Enter value to be added in the list: "))
    l1.append(num)
    total += num
print(l1)
print(total)
