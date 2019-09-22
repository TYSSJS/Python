#DECORATOR
def outer(func):
    def inner():
        print("inside inner")
        func()
    return inner()

@outer
def sample():
    print("inside sample")
#o/p=
# inside inner
# inside sample

#
#
# #DECORATOE CHAINING
#
# print("decorator chaining")
#
# def outer(fun):
#     def inner():
#         print("inside inner")
#         fun()
#     return inner
#
# def outer1(func):
#     def inner():
#         print("inside inner")
#         func()
#     return inner
#
# @outer
# @outer1
# def sample():
#     print("inside sample")
# sample()


#
#
#way -2 Decorator
def out(fu):
    def inn():
        fu()
    return inn

def sample():
    print("The end")
a=out(sample)
a()



# def out(fu):
#     def inn():
#         fu()
#     return inn
#
# def sample():
#     print("The end")
# a=out(sample)
# a()


#decorator by variable

class A:
    a=70
    @classmethod
    def m1(cls):
        print(cls.a)

o=A()
o.m1()

