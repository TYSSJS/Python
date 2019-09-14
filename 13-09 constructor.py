# class const:
#     def __init__(self, name, age):
#         self.Name = name  # Name,Age - local variable and we are assigning while calling the method
#         self.Age = age
#
#     def display(self):
#         print(self.Name, self.Age)
#
# obj = const('kimi', 12)
# obj.display()

# class demo():
#     def __init__(self, name, age):
#         self.Name = name  # Name,Age - local variable and we are assigning while calling the method
#         self.Age = age
#
#     def info(self, add):
#         self.Add = add
#         print(self.Name, self.Age, self.Add)
#
# obj = demo('kimi', 12)
# obj.info('bang')

class Demo():
    def list(self, a, b):
        l = []
        for i in range(a, b):
            l.append(i)


        print(l)
Demo().list(0,10)

# class Demo1():
#     def add(self, a, b):
#         for i in range(a, b):
#             sum = a + b
#             a = b
#             b = sum
#         print(sum)
#
# obj = Demo1()
# obj.add(1, 10)
