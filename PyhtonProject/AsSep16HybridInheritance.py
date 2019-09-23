class Tree():
    def t(self):
        print("this is tree")

class AppleTree(Tree):
    def at(self):
        print("this is apple tree")

class MangoTree(Tree):
    def mt(self):
        print("this is mango tree")

class Fruit(AppleTree,MangoTree):
    def f(self):
        print("this is fruit")


obj = Fruit()
obj.t()
obj.at()
obj.mt()
obj.f()