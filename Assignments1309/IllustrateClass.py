class Dog:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

    def wag_tail(self):
        print("wagging tail")

    def bark(self):
        print("barking")


d1 = Dog('black', 'german sheperd')
d1.wag_tail()
