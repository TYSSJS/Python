# print("Question No.5")
# #5. WAP to perform square root of a given number.
# class SquareRoot():
#     def square(self):
#         num=int(input("Enter a number"))
#         square=num*num
#         print("Square root of this number is=",square)
# obj=SquareRoot()
# obj.square()
#
# print("Question No.6")
#6 WAP to perform febonacci series in two different ways.(method and in-built both)
# print("Febonacci series using simple method")
# n=int(input("Enter a Range of number"))
# febo=0
# def febo(n):
#     a=0
#     b=1
#
#     print(a)
#     print(b)
#     for i in range(n):
#         c=a+b
#         print(c)
#         a,b=b,a+b
# febo(10)
#
# print(" ")
#
# print("Febonacci series using in-built package")
# import math as n
# print(n.factorial(4))
#
# print(" ")
# print("Question No.7")
# #7 Generate a random numbers from range 0to9- any one number to be diaplayed
# import random as r
# for i in range(1):
#     print("Random any one number",r.randint(0,9))
# print(" ")
# print("Question No.8")
#8 Generate 10 different phone numbers using libraries or modules.
# import random as r
# print("Random phone numbers")
# for i in range(1,11):
#     for j in range(0,10):
#         print(r.randrange(0,9),end=' ')
#     print(" ")


# NORMAL CODE:
# new_list=[]
# old_list=[1,2,4,5,6]
# for i in old_list:
#     if(i%2==0):
#         new_list.append(i)
# print(new_list)
#
# LIST COMPREHENSION CODE:
# new_list=print([i for i in old_list if(i%2==0)])


# import calendar
# print(calendar.month(2019,5))

# def fibR(n):
#     if n==1 or n==2:
#         return 1
#         return fibR(n-1)+fibR(n-2)
# print(fibR(2))

a,b = 0,1
def fibI(n):
    global a,b
    while True:
        a,b = b,a+b
    yield a+b
f=fibI(5)
print(f.__next__())


