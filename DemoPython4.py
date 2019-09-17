######################################################################################################
"""WAP to illustrate class in Python"""
def PyClass():
    print('This is a simple class')

PyClass()
######################################################################################################
"""WAP to display even numbers using list comprehension"""
print([i for i in range(1, 101) if i%2 == 0])
######################################################################################################
"""Accept input from the user and display in dictionary type"""
def CreateDictionary(n, di):
    for i in range(int(n)):
        ip = input('Enter dictionary key-value pair separated by :')
        key, value = ip.split(":")
        di[key] = value
    print(di)
n = input('Enter the total number of dictionary key-value pairs')
di = {}
CreateDictionary(n, di)
######################################################################################################
"""A program to read customer bank info and demo a credit/debit scenario"""
li = []
# li = ['Name', 'A/C Number', 'Balance', 'VK', '1234', '350,000', 'MK', '5678', '380,000']
def custAdd():
    for i in range(0, 3):
        if i > 0:
            print('Enter customer ', i, ' details in the header order:')
        for j in range(0, 3):
            if i == 0:
                obj = input('Enter header value one by one:')
                li.append(obj)
            elif i > 0:
                obj = input()
                li.append(obj)
    print(li)
custAdd()
print(li.index('VK'))
print(li[li.index('VK')+2])

def creditDebit(st, credeb):
    preBal = int((li[li.index(st)+2]))
    newBal = preBal + (int(credeb))
    print('Amount ', credeb, ' has been credited/debited and the new balance is ', newBal)

st = input('Enter the account holder name')
credeb = input('Enter amount to be credited/debited(-number)')

creditDebit(st, credeb)
######################################################################################################
"""Fetch employee details from a list of tables"""
di = {'001':['Viraat', 'Pre-K', 'Klay-Jayanagar', 'Bengaluru'], '002':['Manvita', 'Grade 3', 'Kendriya Vidyalaya', 'Ballari'], '003':['Samarth', 'Grade 1', "People's Tree", "Ballari"]}
def fetching(k):
    print(di.get(k))
k = input('Enter student ID to fetch details')
fetching(k)
######################################################################################################
"""User enters TYSS, display 'Welcome toPython' message"""
di = {'TYSS':'Welcome to Python', 'JSP':'Welcome to Java'}

def display():
    st = input('Enter string to fetch the message')
    print(di.get(st))
display()
######################################################################################################
"""WAP to calculate summation of given numbers"""
n = input('Enter how many numbers to be added:')
li = []
num = 0
def addNum(n, num):
    for i in range(0, int(n)):
        m = input('Enter numbers one by one: ')
        li.append(m)
        num = int(num) + int(m)
    print('Given list is ', li)
    print('Summation of entered numbers is ', num)
addNum(n, num)
######################################################################################################
"""Enter name of trainee, get his/her stream"""
di = {'Prakash':'JS', 'Manish':'JS', 'Satyashree':'JS', 'JRKashyap':'Python', 'Prahsanth':'Python', 'Shreyas':'Python'}
print(di.get('Manish'))
######################################################################################################
"""WAP to demonstrate all assignment operators"""
a = 10
b = 12

if a == b:
    print('a is equals to b')
elif a >= b:
    print('a is greater than or equals b')
elif a <= b:
    print('b is greater than or equal to a')
###########################################################################################################
"""WAP to demo all data types in Python"""
di = {'a':10, 'b':12.4, 'c':'Python', 'd':1+2j, 'e':[1,2,3], 'f':(1, 'Guido van Rossum'), 'g':{9, 8, 7, 0}}

print(type(di['a']))
print(type(di['b']))
print(type(di['c']))
print(type(di['d']))
print(type(di['e']))
print(type(di['f']))
print(type(di['g']))
print(type(di))
###########################################################################################################
"Read user i/p in a list and print sum of all list elements"
li = []
sum = 0
s = input('Enter list size of the list: ')
for i in range(int(s)):
    e = input('Enter list elements one by one: ')
    sum = sum + int(e)
    li.append(e)
print('\n User entered list elements are: \n ', li, '\n Sum of elements: \n ', sum)
###########################################################################################################
"""Count the numbers in string '10a1b2c3d5' """
st = '10a1b2c3d5'
str = ''
for i in range(len(st)):
    if st[i].isnumeric():
        str = str + st[i]
    else:
        continue
print('Given string is ', st, '\n Numbers in the string are: ', str)
###########################################################################################################
"""WAP to find given year is leap or not"""
y = int(input('Enter the year please'))
if(y % 4 == 0):
    if(y % 100 == 0):
        if(y % 400 == 0):
            print(y,' is a leap year')
        else:
            print(y, " isn't a leap year")
    else:
        print(y, ' is a leap year')
else:
    print(y, " isn't a leap year")
"""Using calender library in-built method"""
import calendar as cal
y =2000
print(cal.isleap(y))
###########################################################################################################
"""WAP to check largest even number in the list"""
li = [1, 11, 2, 5, 4, 3, 6, 9, 10, 8, 7]
print(li)
li.sort()
lastInd = len(li)-1
for i in range(lastInd):
    if li[lastInd] % 2 ==0:
        print(li[lastInd], " is the highest even number in the list")
        break
    else:
        lastInd = lastInd - 1
        continue
###########################################################################################################
"""WAP to count the lowercase letters in a given string"""
st = 'Test Yantra Software Solutions Private Limited'
caseCount = 0
for i in range(len(st)):
    if st[i].islower():
        caseCount = caseCount + 1
    else:
        continue
print('Total lower case letters in the given string is: ', caseCount)
###########################################################################################################
"""WAP to check whether a given key is present in the dictionary"""
di = {0:'JR Kashyap', 1:'Viraat Kashyap', 2:'Ramyashree'}
k = input('Enter a dictionary key to check')
for i in range(len(di)):
    if (di[int(k)]):
        print('Key is valid and present')
        break
###########################################################################################################
"""WAP to check strong number"""
import math as m
num = 145
n = str(num)
dig = 0
res = 0
for i in range(len(n)):
    dig = int(n) % 10
    n = int(n) // 10
    res = res + m.factorial(dig)
if num == res:
    print("It's a strong number")
else:
    print('Not a strong number')
###########################################################################################################
"""WAP to print numbers that're not divisible by 2,3 and 7 in the range 43 to 958"""
print([i for i in range(43, 959) if (i%2 != 0 and i%3 != 0 and i%7 !=0)])
