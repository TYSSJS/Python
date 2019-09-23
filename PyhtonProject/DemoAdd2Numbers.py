class AddNumbers():
    def add(self):
        print(self.a + self.b)
    def __init__(self, a, b):
        self.a = a
        self.b = b
obj = AddNumbers(5,6)
obj.add()
