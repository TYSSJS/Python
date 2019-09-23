class a():
    def m1(self):
        print("in parent class")

class b(a):
    def m2(self):
        print("in child class")

class c(b):
    def m3(self):
        print("in child'd child class")

obj = c()
obj.m1()
obj.m2()
obj.m3()