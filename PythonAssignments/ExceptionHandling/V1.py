class A:
    a=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def m1(self,z):
        print(self.a,z)
        l=100
        print("local var",l)
o=A(1,4)
print(o.a)
o.a=50
o.m1(12)
o1=A(10,20)
o1.m1(500)
print(o1.a)