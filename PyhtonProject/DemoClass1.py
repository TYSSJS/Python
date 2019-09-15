class Sample():

    #constructor
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print(self.name, self.address)


#object creation
obj = Sample("surbhi", "bangalore")
obj.display()