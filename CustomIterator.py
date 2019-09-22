class hotel:
    def __init__(self):
        self.menu=["idly","vada","chai","panipuri"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index >= len(self.menu):
            raise StopIteration
        return self.menu[self.index]


# obj=hotel()
# i=iter(obj)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

for i in hotel():
    print(i)



