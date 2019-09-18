# 1:single level inheritance

# class A():
#     def f1(self):
#         print("parent class A")
# class B(A):
#     def f2(self):
#         print("child B")
# o=B()
# o.f1()
# o.f2()

# 2:multilevel inheritance
# class A():
#     def f1(self):
#         print("parent class A")
# class B(A):
#     def f2(self):
#         print("child B")
# class C(B):
#     def f3(self):
#         print("child C")
# o=C()
# o.f1()
# o.f2()
# o.f3()

# Hierarchial
# class A():
#     def f1(self):
#         print("parent class A")
# class B(A):
#     def f2(self):
#         print("child B")
# class C(A):
#     def f3(self):
#         print("child C")
# o=C()
# o.f1()
# o.f3()

# 4:multiple inheritance
# class A():
#     def f1(self):
#         print("parent class A")
# class B():
#     def f2(self):
#         print("child B")
# class C(A,B):
#     def f3(self):
#         print("child C")
# o=C()
# o.f1()
# o.f2()
# o.f3()

#hibrid inheritance
class A():
    def f1(self):
        print("parent class A")
class B(A):
    a=10
    def f2(self):
        print("child B")

class C(A):
    a = 20
    def f2(self):
        print("child C")

class D(B,C):
    def f4(self):
        print("child D")
o=D()
o.f1()
o.f2()
print(o.a)
#o.f3()
o.f4()