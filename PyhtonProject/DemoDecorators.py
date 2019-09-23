def outer(fun):
    print("outer")
    def inner():
        print("inner")
        fun()
    return inner

@outer
def Sample():
    print("inside sample")

Sample()