###########################################################################################
"""WAP to demonstrate all types of inheritance"""
###########################################################################################
from enum import unique
"""Single Inheritance"""
class p():
    def pm(self):
        print('From parent class')
class c(p):
    def cm(self):
        print('From child class')
obj = c()
obj.cm()
obj.pm()

"""Multilevel Inheritance"""
class p():
    def pm(self):
        print('Parent class method')
class c1(p):
    def c1m(self):
        print('Child class method')
class c2(c1):
    def c2m(self):
        print('Grandchild class method')
obj = c2()
obj.pm()
obj.c1m()
obj.c2m()

"""Multiple Inheritance"""
class p1():
    def p1m(self):
        print('1st parent method')
class p2():
    def p2m(self):
        print('2nd parent method')
class c(p1, p2):
    def cm(self):
        print('Child method')
obj = c()
obj.cm()
obj.p2m()
obj.p1m()

"""Heirarchial Inheritance"""
class p():
    def pm(self):
        print('Parent method')
class c1(p):
    def c1m(self):
        print('1st child method')
class c2(p):
    def c2m(self):
        print('2nd child method')
ob1 = c1()
ob1.c1m()
ob1.pm()

ob2 = c2()
ob2.c2m()
ob2.pm()

"""Hybrid Inheritance"""
class p1():
    def p1m(self):
        print('1st parent method')
class p2():
    def p2m(self):
        print('2nd parent method')
class c(p1, p2):
    def cm(self):
        print('Child method')
obj = c()
obj.cm()
obj.p2m()
obj.p1m()

"""Heirarchial Inheritance"""
class p():
    def pm(self):
        print('Parent method')
class c1(p):
    def c1m(self):
        print('1st child method')
class c2(p):
    def c2m(self):
        print('2nd child method')
class d(c1, c2):
    def dm(self):
        print('Last Grandchild method')
ob3 = d()
ob3.pm()
ob3.c1m()
ob3.c2m()
ob3.dm()
###########################################################################################
"""Constructor example"""
class Practice():
    def __init__(self, str):
        print(str)
ob = Practice('Hello World!')
###########################################################################################
"""Method Overloading"""
class Mo():
    def m1(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            print(int(a + b + c))
        elif a != None and b != None:
            print(int(a + b))
        else:
            print('Kindly enter at least 2 arguments to execute method')
t = Mo()
t.m1(2, 3, 4)
t.m1(2, 3)
t.m1(4)
###########################################################################################
"Method Overloading using variable length argument(*a is always of tuple type)"
class Mo():
    def sum(self, *a):
        total = ''
        for x in a:
            total = total + x
        print('Concatenated string is : ', total)
t = Mo()
t.sum('Hello ', 'Wrold!')
t.sum('Hello', ' Python', ' Wrold!')
###########################################################################################
"""Method Overriding"""
class P():
    def Treasury(self):
        print('cash, land, cars, gold')
    def marry(self):
        print('Javaramma')
class C(P):
    def marry(self):
        super().marry()
        print('Neha')
t = C()
t.Treasury()
t.marry()
###########################################################################################
"""WAP to perform square root of a given number"""
import math as m
n = 81
print(m.sqrt(n))
###########################################################################################
"""WAP to find fibo of a given number"""
def fib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return fib(n-1) + fib(n-2)
print(fib(8))
###########################################################################################
"""WAP to generate random numbers in the range 0 to 10"""
import random as r
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
randNum = r. randint(len(li)-len(li), len(li)-1)
print(randNum)
###########################################################################################
"""WAP to generate 10 different phone numbers"""
import random as r
n = '9876543210'
for i in range(0, 10):
    for j in range(0, 10):
        phNum = r.randint(0, len(n)-1)
        print(phNum, end = '')
    print()
###########################################################################################
"""W5P to demonstrate lambda expressions in Python"""
import math as m
"""Lambda 1"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = lambda l:l%2 == 0
print(even(6))

"""Lambda 2"""
odd = lambda l:l%2 != 0
print(odd(5))

"""Lambda 3"""
squareRoot = lambda l:m.sqrt(l)
print(squareRoot(4))

"""Lambda 4"""
power = lambda l:m.pow(l, 3)
print(power(2))

"""Lambda 5"""
square = lambda l:l*l
print(square(2))
###########################################################################################
"""Read a file and print data on console"""
f = open('Textfile2.txt', 'r')
data = f.readline()
print('File data is ', data)
###########################################################################################
"""Write data onto the existing file that's not empty"""
f = open('Textfile.txt', 'w')
data = 'East or West, India is the best'
f.write(data)

f = open('Textfile.txt', 'r')
data = f.read()
print(data)
###########################################################################################
"""WAP read data from the file and print only 7 lines"""
import linecache
f = open('Textfile2.txt', 'w')
data = ("Kaveri of Karnataka\n", "Tungabhadra of Karnataka\n", "Hemavathi of Karnataka\n", "Kapila of Karnataka\n", "Arkavathi of Karnataka\n", "Netravathi of Karnataka\n", "Krishna of Karnataka\n", "Seetha of Karnataka\n", "Kumaradhara of Karnataka\n")
f.writelines(data)

f = open('Textfile2.txt', 'r')
data = f.read()
for i in range(1,8):
       print(linecache.getline('Textfile2.txt', i))
###########################################################################################
""""WAP to count total words in a file"""
f = open('Textfile2.txt', 'r')
data1 = f.read()
for i in range(len(data1)):
       words = data1.split()
print(len(words))
###########################################################################################
"""WAP to print the 1st character of the file"""
f = open('Textfile2.txt', 'r')
dat = f.read()
print(dat[0])
###########################################################################################
"""WAP to display common letters present in two given strings"""
st1 = input('Enter 1st string')
st2  = input('Enter 2nd string')
for i in range(0, len(st1)-1):
    for j in range(0, len(st2)-1):
        if st1[i] == st2[j]:
            print(st1[i], end=' ')
###########################################################################################
"""WAP to demonstrate bubble sort"""
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end = ' ')
###########################################################################################
"""WAP to count unique words in a file"""
from collections import OrderedDict
f = open('Textfile2.txt', 'r')
count = 0
num_lines = sum(1 for line in open('Textfile2.txt'))

li = []
data1 = f.read()
for i in range(num_lines):
    words = data1.split()
    if i == num_lines-1:
        for j in range(0, len(words)):
            li.append(words[j])
print('Unique words in file are: ', len(list(OrderedDict.fromkeys(li))), '\nUnique words are as follows: ',list(OrderedDict.fromkeys(li)))
###########################################################################################
"""WAP to print the file in reverse order """
for line in reversed(list(open('Textfile2.txt'))):
    print(line.rstrip())
###########################################################################################
"""WAP to create a file, perform addition, multiplication, division and call that fil in another file using import"""
from TYAnushree.DemoPython3 import add, subtract, multiply
print(add(4, 5))
print(subtract(5, 4))
print(multiply(2, 3))
###########################################################################################
"""WAP to count how many a times a word or letter has appeared"""
from collections import Counter
f = open('Textfile2.txt', 'r')
count = 0
num_lines = sum(1 for line in open('Textfile2.txt'))
li = []
st = 'Om Namo Narayanaya'
data1 = f.read()
for i in range(num_lines):
    words = data1.split()
    if i == num_lines-1:
        for j in range(0, len(words)):
            li.append(words[j])
a = dict(Counter(li))
b = dict(Counter(st))
print(a)
print(b)
###########################################################################################
"""WAP to append the contents of one file to another file"""
f = open('Textfile.txt', 'r')
data = f.read()

f= open('Textfile2.txt', 'a+')
f.write(data)
f.flush()

f = open('Textfile2.txt', 'r')
dat = f.read()
print(dat)
###########################################################################################
"""WAP to count the number of blank spaces in a text file"""
from collections import Counter
f = open('Textfile.txt', 'r')
fdat = f.read()
a = dict(Counter(fdat))
print('Total number of blank spaces in the file is: ', a.get(' '))
###########################################################################################
"""WAP read a file and capitalize the 1st letter of every word"""
f = open('Textfile.txt', 'r')
fdat = f.read()
print(fdat.title())
###########################################################################################