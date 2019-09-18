# Hierarical inheritance
class p:
    def m1(self):
        print("In parent method")

class c1(p):
    def m2(self):
        print("in c1 method")

class c2(p):
    def m3(self):
        print("in c2 method")

o1=c1()# c1 can only inherit from parent
o1.m1()
o1.m2()

o2=c2() #c2 can only inherit from parent
o2.m1()
o2.m3()