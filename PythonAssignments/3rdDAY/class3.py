#multilevel inheritance
# class a():
#     def m1(self):
#         print("frome parent class")
# class b(a):
#     def m2(self):
#         print("from child class")
# class c(b):
#     def m3(self):
#         print("from child's child class")
# o= c()
# o.m1()
# o.m2()
# o.m3()


class a():
    """ hirarchi...inheritance
    """
    # '''DOCUMENTATIN STRING->hirarchial inheritance'''
    def m1(self):
        print("parent")
class b(a):
    def m2(self):
        print("from b child")
class c(a):
    def m3(self):
        print("from c child")
print(__doc__)
o1=c()
o1.m1()
o1.m3()

# multiple inheritance
class x():
    def x1(self):
        print("parent class x")
class y():
    def y1(self):
        print("parent class y")
class z(x,y):
    def z1(self):
        print("from child z class")
obj=z()
obj.x1()
obj.y1()
obj.z1()

# multiple inheritance case 2
class x():
    def x1(self):
        print("parent class x")
class y():
    def x1(self):
        print("parent class y")
class z(x,y):
    def z1(self):
        print("from child z class")
obj=z()
obj.x1()

# multiple inheritance case 3
class x():
    def x1(self):
        print("parent class x")
class y():
    def x1(self):
        print("parent class y")
class z(y,x):
    def z1(self):
        print("from child z class")
obj=z()
obj.x1()
