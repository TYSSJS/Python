class Pen:
    '''DOCUMNETATION STRING --> PEN IS A CLASS AND WRITE IS A METHOD'''
    print(__doc__)
    print("hey")
    length = 10
    color = "white"
    shape = "cylindrical"
    brand = "camlin"
    print("hy")
    def write(self):
        print("pen is writing")
        print(id(self))

    def throw(self):
        print("pen can be thrown")
        print(id(self))

obj = Pen()
print(id(obj ))
print(obj.color)
obj.write()
