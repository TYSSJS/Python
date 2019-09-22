# import math
# print(math.factorial(5))     # 120
#
# import  math as m
# print(m.factorial(4))   #24
#
# from math import factorial
# print(factorial(5))    # 120


#generate factorial series
#yield=for series
#return=for particular num

def genFacto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        yield fact

for i in genFacto(6):
    print(i)




# random numbers
# import random as r
# for i in range(5):
#     print(r.randint(5,500))   #any 5 numbers...dynamically changing like OTP, CAPTCHA, IPAddress


# import calendar
# print(calendar.month(2019, 9))
# print(calendar.day_name.__len__())




