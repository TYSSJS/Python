def outer(f):
    print("h")
    def inner():
        print("hey")
        f()
        print("hello")
    return inner
def sample():
    print("end")
o = outer(sample)
o()
