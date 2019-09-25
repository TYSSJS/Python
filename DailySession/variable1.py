# class A:
#     a=12
#     def m1(self):
#         b=11
#         print("inside m1-->b:",b)
#         print("indide m1-->a:",A.a)# we cannot access global variable directly
# o=A()
# o.m1()
# print(o.a)

class A:
 # if global than we caanot call it after creating the object or class
    global a
    a=12
    def m1(self):
        b=11
        print("inside m1-->b:",b)
        print("indide m1-->a:",a)# if we declare variable as 'global' inside the classs.
#         can be accessed
o=A()
o.m1()
print(o.a)