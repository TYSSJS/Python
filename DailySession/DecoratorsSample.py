def outer(fun):
    def inner():
        fun()
    return inner

def Sample():
    print("the end")

o=outer(Sample)
o()