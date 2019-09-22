class A:
    def __init__(self):
        print("Moring mam will kill us")

class B(A):
    def __init__(self):
        super().__init__()
        print("Afternoon we will enjoy")
        A.__init__(self)

obj=B()