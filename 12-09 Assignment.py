a = input("Enter Value")
b = input("Enter Value")
c = input("Enter Value")
print(a)
print(b)

print(" ")

if a > b:
    print("a is greater")
else:
    print("b is greater")

print(" ")

if a > b:
    if (a > c):
        print("a is greater")
    else:
        print("c is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")

print(" ")

x = int(input("enter a number"))
if x in range(0, 10):
    if x == 0:
        print("zero")
    elif x == 1:
        print("one")
    elif x == 2:
        print("two")
    elif x == 3:
        print("three")
    elif x == 4:
        print("four")
    elif x == 5:
        print("five")
    elif x == 6:
        print("six")
    elif x == 7:
        print("seven")
    elif x == 8:
        print("eight")
    elif x == 9:
        print("nine")
else:
    print("enter proper number")

print(" ")

 s=input("enter a line")
print(s)
for i in range(1, len(s)):
    print(s[i], end=",")

for i in range(1, len(s)):
    if s[i] in range(ord('a'), ord('z')):
        print("alpha ", s[i])
    for n in range(0, 9):
        if s[i].__contains__(str(n)):
            print("number ", s[i])
    else:
        print("symbol", s[i])
print(" ")

def emp(name, id, dept, sal):
    print("emp name-", name, "\n","id-",id,"\n","department-",dept,"\n","sal-",sal)


emp("saloni", 10, "test", 5000)
print(" ")
emp("annu", 20, "dev", 6000)
print(" ")
emp("afifa", 30, "autotesting", 7000)
print(" ")
emp("mani", 40, "testing", 8000)
print(" ")
emp("pipa", 50, "dev", 4300)

s = input("enter name")
for i in range(0, len(s)):
    print(s[i], "-", i + 1, "char")

print(" ")

l=[]
def emp(name, id, dept, sal):
    l.append(sal)
    return["emp name-", name, "\n","id-",id,"\n","department-",dept,"\n","sal-",sal]

print(" ")

e1=emp("mani", 40, "testing", 8000)
s1=e1[10]
e2=emp("mani", 40, "testing", 3000)
s2=e2[10]
if s1>s2:
    print(s1," is greater")
else:
    print(s2," is greater")

print(" ")

l=[]
def emp(name, id, dept, sal):
    l.append(sal)
    print("emp name-", name, "\n","id-",id,"\n","department-",dept,"\n","sal-",sal)

emp("mani", 40, "testing", 8000)

emp("manisa", 40, "testing", 3000)
print(l)
if l[0]>l[1]:
    print(l[0]," is greater")
else:
    print(l[1]," is greater")
print(" ")

for i in range(1,51):
    if(i%5==0):
        print(i,end=" ")
print(" ")
for i in range(200,999):
    if(i%5==0):
        if(i%10==0):
            if(i%15==0):
                print(i,end=" ")


print(" ")

l=[12,13]
a=12
b=13
print("a",a,"b",b)
a=a+b
b=a-b
a=a-b
print(a)
print(b)
print("a",a,"b",b)

print(" ")

a=123957
# print(a // 10)
# print(a % 10)
for i in range(0,(a%10)-1):
        print(a % 10,end=" ")
        a=a//10

print(" ")

p=12000
t=2
r=4
s=((p*t*r)//100)
print(s)

print(" ")

l1=[1,2,3,4]
l2=[9,8,7,6]
l1.extend(l2)
print(l1)
l3=[10,23,34]
l3.append(l1)
print(l3)

print(" ")

s="afifa"
rev=s[::-1]
if (s == rev):
    print("palindrome")
else:
print("not a palindrome")

print(" ")

l=[]
s="salouaani"
for i in range(0, len(s)):
    if s[i].__contains__("a") or s[i].__contains__("e") or s[i].__contains__("i") or s[i].__contains__("o") or s[i].__contains__("u"):
        print(s[i], "vowel")
        l.append(s[i])
    else:
        print(s[i], "consonant")

print(len(l))

print(" ")

l=[1,2,3,4,5,6]
a=l[0]
b=l[1]
c=l[len(l)-1]
d=l[len(l)-2]
l[0]=d
l[1]=c
l[len(l)-1]=b
l[len(l)-2]=a
print(l)

print(" ")

newList = [12, 35, 9, 56, 24]
size = len(newList)
temp = newList[0]
newList[0] = newList[size - 1]
newList[size - 1] = temp

print(" ")


temp = newList[1]
newList[1] = newList[size - 2]
newList[size - 2] = temp
print(l)

print(" ")

str=input("enter a string")
print("letter are ")
for i in str:
    if (ord(i) >=97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        print(i, end=" ")
print("\n")
print("numbers are ")
for i in str:
    if (ord(i) >= 48 and ord(i) <= 57):
        print(i, end=" ")
print("\n")
print("symbols are")
for i in str:
     if (ord(i) >= 32 and ord(i) <= 47):
         print(i, end=" ")
