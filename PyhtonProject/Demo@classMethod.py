class A():
    a = 10
    @classmethod
    def m1(cls):
        print(cls.a)
        print(A.a)
    def m2(self):
        print(A.a)

o = A()
o.m1()
o.m2()