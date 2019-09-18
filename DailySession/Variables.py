class A:
    a=10 #static variable
    def __init__(self,a,b):
        self.a=a #instance variable, will create a object of class.
        self.b=b
    def m1(self,z):
        print("The value of A to Z",self.a,z)
        l=10 #local variable
        print("local variable",l)
o=A(10,20)
o.a
o.m1(20)