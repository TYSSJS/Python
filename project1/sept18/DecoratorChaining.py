def outer(fa):
    print("outer")
    def inner():
        print("start")
        fa()
    return inner

def outer1(fa):
    print("outer1")
    def inner():
        print("starting")
        fa()
    return inner
@outer
@outer1
def sample():
    print("end")
sample()