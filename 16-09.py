# #single inheritance
# class p():
#     def m1(self):
#         print("in parent class")
# class c(p):
#     def m2(self):
#         print("in child class")
# obj=c()
# obj.m1()
# obj.m2()
#
# # Multilevel inheritance
# class p():
#     def m1(self):
#         print("in parent class")
# class c(p):
#     def m2(self):
#         print("in child class")
# class d(c):
#     def m3(self):
#         print("in child's child class")
# obj=d()
# obj.m1()
# obj.m2()
# obj.m3()
# #Hierarchical inheritance
# class p():
#     def m1(self):
#         print("in parent class")
# class c1(p):
#     def m2(self):
#         print("in c1 class")
# class c2(p):
#     def m3(self):
#         print("in c2 class")
# obj1=c1()
# obj1.m1()
# obj1.m2()
#
# obj2=c2()
# obj2.m1()
# obj2.m3()
#
# #multiple inheritance
# class p1():
#     def m1(self):
#         print("in method p1")
# class p2():
#     def m2(self):
#         print("in method p2")
# class c(p1,p2):
#     def m3(self):
#         print("in child class")
# obj=c()
# obj.m1()
# obj.m2()
# obj.m3()
# #if 2 methods are same in 2 diff class
# class p1():
#     def m1(self):
#         print("in method p1")
# class p2():
#     def m1(self):
#         print("in method p2")
# class c(p1,p2):
#     def m3(self):
#         print("in child class")
# obj=c()
# obj.m1()
# obj.m3()
#
# #Method Overloading
# def add(a,b):
#     print(a+b)
# def add(a,b,c):
#     print(a+b+c)
# def add(a,b,c,d):
#     print(a+b+c+d)
# add(1,2)
#to overcome
# def add(a,b,c=None,d=None):
#     if c==None and d==None:
#         return a+b
#     elif c==None and d!=None:
#         return a+b+d
#     elif c!=None and d==None:
#         return a+b+c
#     else:
#         return a+b+c+d
# print(add(1,2))
# print(add(1,2,3))
# print(add(1,2,3,4))
# print(add(1,2,None,3))

#factorial
# import math as m  #giving allias to math module
# print(m.factorial(4))

#importing only one method from entire package
# from math import factorial
# print(factorial(8))

#random
# import random as r
# for i in range(5):
#     print(r.randint(5,500))

#print calendar
import calendar as c
print(c.month(2019,9))



