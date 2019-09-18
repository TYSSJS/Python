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
print("Febonacci series using simple method")
# n=int(input("Enter a Range of number"))
# febo=0
def febo(n):
    a=0
    b=1

    print(a)
    print(b)
    for i in range(n):
        c=a+b
        print(c)
        a,b=b,a+b
febo(10)
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
print("Question No.8")
#8 Generate 10 different phone numbers using libraries or modules.
import random as r
print("Random phone numbers")
for i in range(1,11):
    for j in range(0,10):
        print(r.randrange(0,9),end=' ')
    print(" ")



