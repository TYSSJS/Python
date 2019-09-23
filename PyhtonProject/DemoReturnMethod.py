def outer():
    print("hi")
    def inner():
        print("inner")
    return inner

o = outer()
o()

