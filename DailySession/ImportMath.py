print("Math package")
import math  as  m
print(m.factorial(4))
# factorial in one line

# Syntax to call perticular method in the package
# import moduleName
# from <Module name> import <Method name>
from math import factorial
print("factorial by importing to math package= ",factorial(12))

print(" ")
print("Random package")
import random as r
for i in range(5):
     print(r.randint(5,500))

print(" ")
print("Calendar package:")
import calendar
print(calendar.month(2019,9))
# month(year,date)

import numbers
