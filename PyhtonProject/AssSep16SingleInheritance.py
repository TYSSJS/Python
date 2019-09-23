class Tree():
    def wind(self):
        print("wind can blow")

class MangoTree(Tree):
    def tasty(self):
        print("mango's are tasty")

obj = MangoTree()
obj.wind()
obj.tasty()