def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        yield fact
        print("end")

for i in Factorial(4):
    print(i)