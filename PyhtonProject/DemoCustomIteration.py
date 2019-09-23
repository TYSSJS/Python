class Hotel():
    def __init__(self):
        self.menu = ["idli", "dosa","vada"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index >= len(self.menu):
            raise StopIteration
        return self.menu[self.index]

o = Hotel()
it = iter(o)
# print(next(i))
# print(next(i))000
# print(next(i))

for i in it:
    print(i)

for i in Hotel():
    print(i)
