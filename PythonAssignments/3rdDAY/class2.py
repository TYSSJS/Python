class employee:
    ''' DCUMENTATION STRING --employee is a class.......'''
    print(__doc__)

    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def dancing(self):
        print(self.name,self.addr)
        print("dancing")

e1=employee("Sara","asdff")
print(e1.addr)
# e1.dancing()


