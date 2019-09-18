# GENERATORS, we use yield
# Fibonacci series
def fib(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
for i in fib(100):
    print(i)