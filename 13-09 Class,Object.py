class pen:
    """ DOCUMENTATION STRING --> PEN IS A CLASS AND WRITE IS METHOD """  # DOC STRING
    print(__doc__)      # print doc string
    print("hi")
    brand='camblin'
    color= 'black'
    def write(self):
        print(id(self))
        print("i m writting")
    def smell(self):
        print(id(self))
        print("smells good")
        pen.color="white"
        pen.color = "red"
        print(self.color)
        print("hello")
    print("bye")
print("die")
# obj=pen()
# obj.write()     # i m writting
# print(id(obj))      # 1302711137784
#
# obj1 = pen()      # object2 created and self contain this add
# print(id(obj1))     # 1302711137840
# obj1.smell()    # smells good
# print(obj1.brand)  # camblin
# print(obj.color)  # black
# obj.smell()
print(pen().color)
pen().smell()