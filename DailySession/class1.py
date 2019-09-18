class pen:
    '''DOCUMENTATION STRING --> PEN IS A CLASS AND WRITE IS A METHOD'''
    print(__doc__)
    brand='camlin'
    color='black'

    def write(amrita):
        print("pen is writing")
    def smell(self):
        print("ink have smell")
        print(id(self))
        print(pen.brand)
        print(__doc__)
obj=pen() #same address will be present for object and self
# object is pointing to the class
# and self point to the object.
# if self is pointing to the different object , it will take that object address
print(id(obj))
obj1=pen()
print(obj.color)
obj.write()
print(obj1.brand)
obj.smell()