class A():
    def __init__(self):
        print("morning i will kill u")

class B(A):
    def __init__(self):
       super().__init__() # calling constructor of super class
       #A.__init__(self)
       print("afternoon full enjoyment")

o = B()
