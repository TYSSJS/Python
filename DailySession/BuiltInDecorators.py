class A:
    a=10
    @classmethod
    def m1(cls):
        print("a=",cls.a)
o=A()
o.m1()
print(A.a)

class Animal:
    legs=4
    @classmethod
    def info(cls,name):
        print("{1} with {0} legs".format(name,cls.legs))
        print("{} with {} legs".format(name, cls.legs))
o=Animal()
o.info("Tiger")