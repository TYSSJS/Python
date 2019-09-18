# Nested method
def outer():
    def add(a,b):
        print("sum of a and b",a+b)
    add(1,2)
    add(2,3)
outer()
# return outer
# add method must be called before outer method
# outer method is mandatory to call
