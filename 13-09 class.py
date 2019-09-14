class pen:
    '''DOCUMENTATION STRING -->PEN IS A CLASS AND WRITE IS A METHOD'''  #it is a documentation of string
    print(__doc__)
    brand='camlin'
    color='white'
    def write(self):    #self contains current object address
        print("we are writing using pen")
        self.color='black'          #initializing to new color using self which acts like this keyword in java
        print(self.color)           #black
        print(id(self))
    def smell(self):
        print("pen smells good")
        print(id(self))
        #print("hi")
    #print("bye")
#print("sii")
obj=pen()
print(obj.brand) #camlin
print(id(obj))  #1891298076264#obj id and self of write mrthod will be having same address
obj.write()
obj1=pen()
print(id(obj1))
print(obj1.color) #white
obj1.smell()      #pen smells good
print(pen().color) #white









