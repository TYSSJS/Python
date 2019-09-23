class Tree():
    def air(self):
        print("through air we are alive")

class MangoTree(Tree):
    def wind(self):
        print("air can wind both are same thing")

class Mango(MangoTree):
    def tasty(self):
        print("mango is tasty")

obj = Mango()
obj.air()
obj.wind()
obj.tasty()