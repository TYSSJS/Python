""" constructor : is a special member of the class, and it will be called during object creation.
    The purpose of constructor is to initialise the members of the class and also to create an
    object of that class.
    __init__(selp) method is called as constructor
    selp is default argument for constuctor; it hold the current object address

"""
# EX:
class employee:

    def __init__(self,name,id):
        self.name=name
        self.id=id
    def disp(self):
        print(self.name," ",self.id)
o=employee('sara','1')
o.disp()
