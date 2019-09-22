#DECORATOR
def demo(dec):
    def demo1():
        print("demo1 is an inner method")
        dec()
    return demo1()

@demo
def display():
    print("dispaly method is called by @decorator")



#DECORATOE CHAINING

print("decorator chaining")

def outer(f):
    def inner():
        print("inside inner")
        f()
    return inner

def outer1(h):
    def inner():
        print("inside inner")
        h()
    return inner

@outer
@outer1
def sample():
    print("inside sample")
sample()



# USE OF GENERATOR

def sum():
    print("summation")
    def add(a,b):
        print("in inner method",a+b)
    add(2 ,5)
    return add


var = sum()
var(6,4)        #----->return add