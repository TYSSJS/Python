def outer(fun):
    print("outer")
    def inner():
        print("inner")
        fun()
    return inner

@outer
def sample():
    print("sample")
sample()