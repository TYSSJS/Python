# #SINGELEVEL INHERITANCE:-
# class super:
#     print("this is a super class")
#
#
# class sub(super):
#     print("this is a sub class")
#
# obj=sub()
#
# #MULTILEVEL IN HERITANCE:-
# class super1:
#     def m1(self):
#         print("1st super class")
#
# class super2(super1):
#     def m2(self):
#         print("2nd super class")
#
# class sub(super2):
#     def m3(self):
#         print("it is a sub class")
#
# obj=sub()
# obj.m3()
# obj.m2()
# obj.m1()
#
# # Hierarchical inheritance:-
# class parent():
#     def m1(self):
#         print("grand parent class")
#
# class sub1(parent):
#     def m2(self):
#         print("1st sub class")
#
# class sub2(parent):
#     def m3(self):
#         print("2nd sub class")
#
# obj=sub2()
# obj.m1()
# obj.m3()
# obj=sub1()
# obj.m1()
# obj.m2()
#
#
# # MULTIPLE INHERITANCE:- if here m and m1 are of same name then it will override the 1st method
# class p():
#     def m1(self):
#         print("m in p class")
#
# class p1():
#     def m1(self):
#         print("m1 in p1 class")
#
#
# class p2(p,p1):
#     def m2(self):
#         print("multiple inheritance")
#
# obj=p2()
# obj.m2()
# obj.m1()


#METHOD OVERRIDDING IN INHERITANCE:-
#
class p():
    def m1(self):
        print("m in p class")

class p1():
    def m1(self):
        print("m1 in p1 class")


class p2(p,p1):
    def m2(self):
        print("multiple inheritance")

obj=p2()
obj.m2()
obj.m1()



# #HYBRID INHERITANCE
# class c1():
#     def m1(self):
#         print("Hybrid-main super class")
#
# class c2(c1):
#     def m2(self):
#         print("1sub sub class")
#
# class c3(c1):
#     def m3(self):
#         print(" 2nd sub class")
# class c4(c2,c3):
#     def m4(self):
#         print("sub class")
#
# obj=c4()
# obj.m1()
# obj.m2()
# obj.m3()
# obj.m4()
