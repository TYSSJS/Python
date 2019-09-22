# def outer():
#     def add(a,b):
#         print(a+b)
#     add(2,3)
#
#
# outer()

# def outer():
#     print("outer method")
#     def add():
#         print("inner method")
#     add()
#     return add
#
#
# variable =outer()
# variable()  #----->return add


# class c():
#     def m1(self):
#         print("method-1")
#         def m2():
#             print("method-2")
#         m2()
#         return m2
#
# obj=c()
# obj.m1()
# o=obj.m1()
# o()  #--->return m2
