def outer():
    def inner():
        print("inside a inner method")
    return inner
variable=outer()
variable()
# calling variable() will go directly to the inner method.