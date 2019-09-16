"""Accept 2 numbers from console and display results"""
li = []
for i in range(2):
    a = input("Enter number here:")
    li.append(a)
print(li)
##################################################################################
"""Accept two numbers from user and print the greater"""
a = input("Enter number here:")
b = input("Enter number here:")
if int(a)>int(b):
    print(a, "is greater than ", b)
else:
    print(b, "is greater than ", a)
######################################################################################
"""Accept 3 numbers from user and print the highest"""
l = []
for i in range(3):
    a = input("Enter number here")
    l.append(a)
l.sort()
print(max(l), ' is the highest number')
######################################################################################
"""Enter a number b/w 0 to 9 and display the number in letters"""
li = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
a = input("Enter a number between 0 to 9 here: ")
print(li.pop(int(a)))
######################################################################################
"""Get username and print characters seperately"""
a = input("Enter a simple username: ")
for i in range(len(a)):
    print(a[i])
######################################################################################
"""Separate letters, numbers and special characters from a given string"""
a = input("Enter a sting that contains special characters")
alpha = []
numeric = []
special = []
for i in range(len(a)):
    if(a[i].isalpha()):
        alpha.append(a[i])
    elif(a[i].isnumeric()):
        numeric.append(a[i])
    else:
        special.append(a[i])
print(alpha,'\n',numeric, '\n', special)
######################################################################################
"""A program to merge two lists and store merged list in a new list"""
l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
l3 = []
print(l1)
print(l2)
l1.extend(l2)
l3.append(l1)
print(l3)
######################################################################################
"""Enter 5 employee details one by one"""
li = [[], [], [], [], []]

def EmpAdd():
    for i in range(0, 6):
        if i > 0:
            print('Enter employee ', i, ' details in the header order:')
        for j in range(0, 5):
            if i == 0:
                obj = input('Enter header value one by one:')
                li.append(obj)
            elif i > 0:
                obj = input()
                li.append(obj)
EmpAdd()
######################################################################################
"""Compare salaries of two employees and display greater"""
li = []
def EmpAdd():
    for i in range(0, 3):
        for j in range(0, 2):
            if i == 0:
                print('Enter header values')
                obj = input()
                li.append(obj)
            elif i > 0:
                obj = input('Enter employee details:')
                li.append(obj)
    SalComp(li)
def SalComp(li):
    if (li[3] > li[5]):
        print('1st employee salary is greater')
    else:
        print('2nd employee salary is greater')
EmpAdd()
######################################################################################
"""Swap 1st two index elements with the last two in a list"""
lsrc = [10, 20, 30, 40, 50, 60]
ldes = []
print(lsrc)
index = len(lsrc) - 2
for i in range(len(lsrc)):
    if i % 2 == 0:
        ldes.insert(i, lsrc[index])
        index  = index + 1
    elif i % 2 == 1:
        ldes.insert(i, lsrc[index])
        index = index - 3
print(ldes)
######################################################################################
"""Print numbers divisible by 5 in the range 1 to 50"""
for i in range(1,51):
    if i%5 == 0:
        print(i, end=' ')
    else:
        continue
######################################################################################
"""In the range 200 to 999, WAP to find numbers divisible by 5, 10 and 15"""
for i in range(200, 1000):
    if(i%5 ==0) and (i%10 ==0) and (i%15 ==0):
        print(i, end=' ')
    else:
        continue
######################################################################################
"""WAP to reverse a given number"""
num = 123456
div = 10
revNum = ''

while num >= 1:
    n = num % div
    revNum = revNum + str(n)
    num = num//div
print(revNum)
#######################################################################################
"""WAP to check whether a given string is palindrome or not"""
st1 = 'MALAYALAM'
revst1 = st1[len(st1)::-1]
if revst1 == st1:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
#######################################################################################
"""Swap 2 numbers withour using temp variabe"""
li = [1, 2, 3, 4]
print(li)
lis = []
index = len(li) -1
for i in range(len(li)):
    if i % 2 == 0:
        lis.insert(i, li[index])
        index = index - 2
    elif i % 2 == 1:
        lis.insert(i, li[index])
        index = index + 1
print(lis)
########################################################################################
"""Count number of vowels in a given string"""
st = "BB ROy Goes to Bombay viA Gateway"
vowSt = "aeiou"
vowCount = 0
for i in range(len(st)):
    for j in range(len(vowSt)):
        if st[i].casefold() == vowSt[j].casefold():
            vowCount = vowCount + 1
print('Total vowels in given string are: ', vowCount)
########################################################################################
"""Calculate simple interest"""
def calSI(p, t, r):
    si = (float(p) * float(t) * float(r))/100
    print(si)
p = input('Enter principal amount')
t = input('Enter tenure in years')
r = input('Enter rate of interest')
calSI(p, t, r)
#######################################################################################
"""WAP to merger 2 lists and store the merged elements in a new list"""

li1 = [1, 2, 3, 4]
li2 = [5, 6, 7, 8]
li3 = []

li3.extend(li1)
li3.extend(li2)

print(li3)
#######################################################################################
"""WAP to perform simple calculaor operations"""
def add(i, j):
    ans = float(i + j)
    return ans
def subtract(i, j):
    ans = float(i - j)
    return ans
def multiply(i, j):
    ans = float(i * j)
    return ans
def division(i, j):
    if(i or j == 0):
        print('zero division is void')
    else:
        ans = float(i / j)
    return ans
def modulus(i, j):
    if (i or j == 0):
        print('zero mod is void')
    else:
        ans = float(i % j)
i = input('Enter 1st operand')
j = input("Enter 2nd operand")

print(add(i, j))
#######################################################################################
"""Demonstrate functions of Tuple, Set and Dictionary"""
tup = (10, 11, 12, 13, 14, 15, 10, 16, 17, 18, 19)
print(tup.index(14))
print(tup.count(10))

se = {11, 22, 33, 44, 55, 66, 77}
se.issubset(se)


di = {1:'VK', 2:'JK', 3:'RA', 4:'MK'}
print(di.get(3))                                                                                                                                                                                                                                                                                                            dd
print(di.values())
print(di.keys())
print(di.popitem())
#######################################################################################