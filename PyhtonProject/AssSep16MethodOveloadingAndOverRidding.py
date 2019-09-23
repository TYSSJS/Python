#Method Overloading is the process where two methods have same name but different signature. In Python Method overloading is not possible
# Method OverRiding is the process where super class and sub class have the same name.

#method overloading
def add(a,b,c=None,d=None):
    if c == None and d == None:
        print(a+b)
    elif c == None and d != None:
        print(a+b+d)
    elif c != None and d == None:
        print(a+b+c)
    else:
        print(a+b+c+d)
add(2,5,6,8)

class A():
    def a(self):
        print("from A")

class B(A):
    def a(self):
        print("from B")
o = B()
o.a()
o1 = A()
o1.a()