
# DECORATORS AND GENERATORS
# DECORATORS:-
def outer(fun):
    def inner():
        print("inner method")
        fun()
    return inner()

@outer
def Sample():
    print("Sample method")

@outer
def Sample1():
    print("Sample1")

# GENERATORS
# Finding the factorial
def genFact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        yield f
    print("hi")
for i in genFact(6):
    print(i)