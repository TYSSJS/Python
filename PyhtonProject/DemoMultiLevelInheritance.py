class a():
    def m1(self):
        print("in a class")
class b():
    def m2(self):
        print("in b class")

class d():
    def m2(self):
        print("in b another class")
class c(a,b):
    def m3(self):
        print("in child class")

class e(b,d):
    def m4(self):
        print("trying")



o = e()
o.m2()
o.m4()