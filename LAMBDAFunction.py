# def add(a,b):
#
#     print(a+b)
#
# x=int(input("enter x value"))
# y=int(input("enter y value"))
# add(x,y)

# def add(a,b):return a+b
# print(add(1,2))
#

#addition
# sum=lambda a,b:a+b
# print(sum(5,2))
#

#factorial

# import math as m
# fact=lambda a:m.factorial(a)
# print(fact(5))

#split a string

# import re as r
# sp=lambda  s:r.split("u",s)
# print(sp("annapurna"))


# li=[14,58,7,201,200,250,258,20,24,132,35]
# for i in range(len(li)):
#     if li[i]%2==0:
#         print(li[i],end=",")

#check a num in a list even or not
# l=[1,2,5,4,7,44]
# even=lambda l:l%2==0
# print(even(l[2]))

# print all even num in a list

# l=[1,2,5,4,7,44]
# a=list(filter(lambda l:l%2==0,l))
# print(a)


#count a char in a string

# import re
# s=input("enter the string-")
# ch=input("enter the character to be found-")
# num=list(filter(lambda s:re.findall(ch,s),s)).__len__()
# print("no of a particular character entered is-", num)


#   Power of a number
# import math as m
# power=lambda a,b:round(m.pow(a,b))
# x=int(input("enter x value-"))
# y=int(input("enter y value-"))
# print("power acc to x,y is-", power(x,y))