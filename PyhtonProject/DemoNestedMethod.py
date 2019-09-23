def outer(c,d):
    def add(a,b):
        print(a+b)
    add(c,d)

outer(2,4)