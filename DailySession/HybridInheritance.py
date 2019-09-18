class p:
    def m1(self):
        print("In parent method")

class c1(p):
    def m2(self):
        print("in c1 method")

class c2(p):
    def m3(self):
        print("in c2 method")

class cc1(c1,c2):
    def m4(self):
        print("can access all the methods")

obj=cc1()
obj.m1()
obj.m2()
obj.m3()
obj.m4()