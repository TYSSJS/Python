class Sample:
    # paramaterized constructor concept
    def __init__(self,name,address):
        self.nm=name
        self.add=address
    def display(self,age):
        print(self.nm,age)
obj=Sample('anu','bangalore')
obj.display(12)
# obj.displayage(27)