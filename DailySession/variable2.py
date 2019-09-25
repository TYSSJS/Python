# Variables are of two types
z=11
class A:
    global a # if global than we caanot call it after creating the object or class
    a=12
    print(z)
    def m1(self):
        b=11
        print(z)
        print("inside m1-->b:",b)
        print("indide m1-->a:",a)# if we declare variable as 'global' inside the classs.
#         can be accessed
o=A()
o.m1()
print(a)
print(z)

class B:
    print(a)
#     we cannot call it outside the class without classname.
# Always use classname.variable