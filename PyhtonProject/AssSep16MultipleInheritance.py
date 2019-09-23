class Father():
    def m1(self):
        print("from papa")

class Mother():
    def m2(self):
        print("from ma")

class Child(Mother,Father):
    def m3(self):
        print("from child")

obj = Child()
obj.m1()
obj.m2()
obj.m3()