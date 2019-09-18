# it will call both outer and inner method
def outer():
    print("hi")
    def inner():
        print("inner")
    return inner()
v=outer()

# it will call only outer method
def outer():
    print("hi")
    def inner():
        print("inner")
    return inner
v=outer()

 # it will call both outer and inner  method
def outer():
    print("hi")
    def inner():
        print("inner")
    return inner
v=outer()
v()