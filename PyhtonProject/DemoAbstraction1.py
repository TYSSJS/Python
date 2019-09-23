from abc import *
-
class B():
    @abstractmethod
    def m2(self):
        pass

o = B()
o.m2()