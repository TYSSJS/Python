# DECORATORS
# outer method will be considered as Decorators
# i.e we are using it for decorating with other methods.
def outer(fun):
    def inner():
        print("inner method")
        fun() #-->1
    return inner()
# fun--> is a variable name, can be given anything
@outer #--2
# which have annotations, that method will be called
def Sample():
    print("Sample method")

@outer
def Sample1():
    print("Sample1")
