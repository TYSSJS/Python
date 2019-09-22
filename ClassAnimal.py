# class Animal:
#     legs=4
#     @classmethod
#     def info(cls,name):
#         print("{} with {} legs" .format(name,cls.legs))
#         cls.legs=8
#         print(cls.legs)
#         print("{} with {} legs".format(name, cls.legs))
#
# o=Animal()
# o.info("abhi")


# class Animal:
#     legs=4
#     @staticmethod
#     def info(name):
#         print("{} with {} legs" .format(name,Animal.legs))
#         Animal.legs=8
#         print("{} with {} legs".format(name, Animal.legs))
#         Animal.legs=12
#         print("{} with {} legs".format(name, Animal.legs))
#
#
# o=Animal()
# o.info("abhi")
#
# o1=Animal()
# o1.info("pattu")
#
# o2=Animal()
# o2.info("anjum")

class cal():
    @staticmethod
    def add(a,b):
        print(a+b)
