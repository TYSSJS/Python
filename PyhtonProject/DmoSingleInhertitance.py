class a():
    def m1(self):
        print("in parent class")

class b(a):
    def m2(self):
        print("in child class")
obj = b()
obj.m1()
obj.m2()