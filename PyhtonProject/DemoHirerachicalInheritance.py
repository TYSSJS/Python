class a():
    def m1(self):
        print("in parent class")

class b(a):
    def m2(self):
        print("in child b class")

class b1(a):
    def m3(self):
        print("in child b1 class")

o = b()
o.m1()
o.m2()

o1 = b1()
o1.m1()
o1.m3()