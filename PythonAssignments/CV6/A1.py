# class A:
#     def __init__(self):
#         print("mrn")
# class B(A):
#     def __init__(self):
#         # super().__init__()
#         A.__init__(self)
#         print("afternoon")
#
# o=B()

f=open("ex.txt","w")
data="hello good morning"
f.write(data)
print("file is created successfuly")