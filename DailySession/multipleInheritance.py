# multiple inheritance
class p1():
    def m1(self):
        print("on parent1 method")

class p2():
    # def m2(self):
    def m1(self):
        print("in parent2 method")
#        if we will rename m2 to m1, child will override and execute

class c(p1,p2):
    # in python execution will happen from left to right always
    # hence m1 method of p1 will be considered.
    def m3(self):
        print("in child class")
# child can inherit all the methods
o=c()
o.m1() # only m1 from paren1 will be exceuted
# o.m2()
o.m3()

