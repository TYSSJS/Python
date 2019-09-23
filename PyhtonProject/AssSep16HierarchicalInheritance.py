class Tree():
    def t(self):
        print("this is tree")

class AppleTree(Tree):
    def at(self):
        print("this is apple tree")

class MangoTree(Tree):
    def mt(self):
        print("this is mango tree")


obj = Tree()
obj.t()

obj1 = MangoTree()
obj1.t()
obj1.mt()

obj2 = AppleTree()
obj2.t()
obj2.at()