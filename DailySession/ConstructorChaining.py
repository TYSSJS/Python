class A:
    def __init__(self):
        print("Morning i will kill")

class B(A):
    def __init__(self):
        #super().__init__()
        A.__init__(self)
        print("Evening we will enjoy")
#         We should always call the super calling statement from the first line of constructor
# We can achieve constructor chaining in two ways
o=B()

        # use this to import to other file