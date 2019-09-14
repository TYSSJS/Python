class pen:
    '''DOCUMENTATION STRING ---> PEN IS A CLASS AND WRITE IS A METHOD'''   # DOC STRING
    print(__doc__)  # DOCUMENTATION STRING ---> PEN IS A CLASS AND WRITE IS A METHOD
    colour = "white"
    price = 10
    len = "10cm"
    def write(self):  #  (self-keyword) contains the address of the object-obj
        print("self address-" ,self)  # address of self- 1887731152712
        print("pen is used to write")
    print(__doc__)

    def smell(self):
        print("he is smelling the pen")
        self.colour="black"
        print("modified in smell-",self.colour)  # modified in smell- black
        pen.colour="red"
    print(__doc__)
obj = pen()
obj1=pen()
print(obj.colour)  #white
print(obj.price)
print(obj.len)
obj.write()     # pen is used to write
obj.smell()     # he is smelling the pen
print(id(obj))  # 1887731152712  -->same as self

print("completely modified-", obj.colour)  #completely modified- black
print(obj.colour) # black
print(obj1.colour) #red

