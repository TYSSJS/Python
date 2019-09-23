def outer(fun):
    print("outer")
    def inner():
        print("inner")
        fun()
    return inner

def outer1(fun):
    print("outer1")
    def inner1():
        print("inner1")
        fun()
    return inner1

@outer
@outer1
def Sample():
    print("inside sample")
Sample()