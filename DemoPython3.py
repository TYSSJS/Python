for i in range(2):
    a = input("Enter number here:")
    print(a)
##################################################################################
a = input("Enter number here:")
b = input("Enter number here:")
if int(a)>int(b):
    print(a, "is greater")
else:
    print(b, "is greater")
######################################################################################
l=[]
for i in range(3):
    a = input("Enter number here")
    l.append(a)
l.sort()
print(max(l))
######################################################################################
li = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
a = input("Enter a number between 0 to 9 here: ")
print(li.pop(int(a)))
######################################################################################
a = input("Enter a simple username: ")
for i in range(len(a)):
    print(a[i])
######################################################################################
a = input("Enter a sting that contains special characters")
for i in range(len(a)):
    if(a[i].isalpha()):
        print(a[i], end=' ')
    elif(a[i].isnumeric()):
        print(a[i], end=' ')
    else:
        print(a[i], end=' ')
######################################################################################
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
l1.extend(l2)
print(l1)
l3=[]
l3.append(l1)
print(l3)
######################################################################################
li = [[], [], [], [], []]

def EmpAdd(obj):
    li.append(obj)

for i in range(0, 6):
    if i > 0:
        print('Enter details of employee:', i)
    for j in range(0, 5):
        if i == 0:
            obj = input('Enter header values one by one:')
            EmpAdd(obj)
        elif i > 0:
            obj = input()
            EmpAdd(obj)
######################################################################################
li=[[],[]]

def EmpAdd(obj):
    li.append(obj)

def SalComp():
    sal1 = li([1],[1])
    sal2 = li([2],[1])
    if (sal1 > sal2):
        print('1st employee salary is greater')
    else:
        print('2nd employee salary is greater')

for i in range(0,3):
    for j in range(0,2):
        if i == 0:
            print('Enter header values')
            obj = input()
            EmpAdd(obj)
        elif i > 0:
            obj = input('Enter employee details:')
            EmpAdd(obj)
print(li)
SalComp()
######################################################################################
def swapPos(li, el0, el1, el4, el5):
    li[0] = el5
    li[1] = el4
    li[4] = el0
    li[5] = el1
    return li
li = [10, 20, 30, 40, 50, 60]
print(li)
el0 = li[0]
el1 = li[1]
el4 = li[4]
el5 = li[5]
swapPos(li, el0, el1, el4, el5)
print(li)
######################################################################################
for i in range(1,51):
    if i%5 == 0:
        print(i, end=' ')
    else:
        continue
######################################################################################
for i in range(200, 1000):
    if(i%5 ==0) and (i%10 ==0) and (i%15 ==0):
        print(i, end=' ')
    else:
        continue
######################################################################################
li = [1,2,3,4]
print(li)
def swapNum(li, n1, n2):
    for i in range(len(li)):
        li[0] = n2
        li[2] = n1
        return li

n1 = li[0]
n2 = li[2]
swapNum(li, n1, n2)
print(li)
######################################################################################
num = 123456
div = 10
revNum = ''

while num >= 1:
    n = num % div
    revNum = revNum + str(n)
    num = num//div
print(revNum)
######################################################################################
st1 = 'OPPORT'
st2 = ''

for i in range(len(st1)):
    for j in range(len(st1), 1):
        if st1[i] == st1[j]:
            st2 = st2 + st1[i]
        else:
            break
if st1 == st2:
    print("It's a palindrome")
else:
    print("It's not a palindrome")