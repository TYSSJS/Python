class Hotel():
    def __init__(self):
        self.menu=['idly','vada','dosa']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index>=len(self.menu):
            raise StopIteration
        return self.menu[self.index]
# o=Hotel()
# i=iter(o)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# o=Hotel()
# itrobj=iter(o)
# for i in itrobj:
#     print(i)

for i in Hotel():
    print(i)