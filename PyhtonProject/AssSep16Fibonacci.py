class Fibonacci():
    def __init__(self, num):
        self.num = num

    def fib(self):
        a = 0
        b = 1
        c = 0
        for i in range(0,self.num):
            c = a+b
            a = b
            b = c
        print(c)

obj = Fibonacci(5)
obj.fib()


import fib

