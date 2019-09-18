# Single level example using class p and child class c
class p():
    def m1(self):
        print("in the parent class")

class c(p):
    def m2(self):
        print("in the child")

# multi-level inheritance between p,c,cc class
class cc(c):
    def m3(self):
        print("in the childs child class")

# obj=c()
# obj.m1()
# obj.m2() # Single inheritance we have to create object og child class
# In multi-inheritance we have to create the object of childs child class and can access all the methods
obj=cc() #childs child object
obj.m1()
obj.m2()
obj.m3()