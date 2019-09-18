class Hotel:
    def __init__(self):
        self.menu=['idly','vada','dosa']
        self.index=-1
    def __iter__(self):
        # mandatory for iteration
        return self
    def __next__(self):
        self.index+=1
        if self.index >= len(self.menu):
            raise StopIteration
        return self.menu[self.index]
# o=Hotel()
# i=iter(o)
# for m in range(len(o.menu)):
#     print(next(i))
for i in Hotel():
    print(i)