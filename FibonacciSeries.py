def fibo(n):
    x, y = 0, 1
    while x < n:
        yield x
        x, y = y, x + y


for i in fibo(100):
    print(i)