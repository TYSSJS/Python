class Animal():
    legs = 4
    @classmethod
    def info(cls, name):
        # cls.legs = 21
        print("{1} with {0} legs".format(name,cls.legs))

o = Animal()
o.info("Tiger")