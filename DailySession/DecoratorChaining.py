# decorating existing function with new features
def outer(fa):
    def inner():
        print("start")
        fa()
    return  inner
def outer1(fa1):
    def inner1():
        print("starting")
        fa1()
    return inner1

@outer1
@outer
def Sample():
    print("end")
Sample()