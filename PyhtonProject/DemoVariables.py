class A():
    a = 10
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def m1(self,z):
        print("z:", self.a,z)
        c = 10
        print("local",c)
o = A(2,3)
o.a
o.m1(3)
