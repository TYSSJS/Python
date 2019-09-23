from abc import *
class A(ABC):
    @abstractmethod
    def m1(self):
        pass

o = A()
o.m1()

