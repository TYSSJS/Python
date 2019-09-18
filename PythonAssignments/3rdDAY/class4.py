#
# def add(a,b):
#     print(a+b)
# def add(a,b,c=0):
#     if c==0:
#         return a+b
#     else:
#         return a+b+c
#     print(a+b+c)
def add(a,b,c=None,d=None):
    if(c==None and d==None):
     print(a+b)
    elif c!=None and d==None:
        print(a+b+c)
    else:
        print(a+b+c+d)

# print(a+b+c+d)
# add(20.5,20.5,10,10)
#
# # n=int(input("enter a number"))
# # f=1
# # while n>0:
# #     f=f*n
# #     n-=1
# # print(f) or
# import math as m
# print(m.factorial(5))

import random as r
for i in range(5):
    print(r.randint(5,500))

from random import randint
print(randint(5000,8000))

from math import factorial
print(factorial(4))

import calendar
print(calendar.month(2019,9))
print(calendar.weekday(2019,9,16))

