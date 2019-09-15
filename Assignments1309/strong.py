a = input("Enter the value")
res = 0
for i in range(len(a)):
    fact = 1
    for x in range(1, int(a[i]) + 1):
        fact = fact * x
    res = res + fact 

if res == int(a):
    print("its a strong no")
else:
    print("not a strong no")
