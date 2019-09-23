num = 1
for i in range(0,4):
    for j in range(0,4):
        if i>=j:
            print(num,end=" ")
            num += 1
    print()