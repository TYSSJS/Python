# 1= read 2 values from user dynamically and print in console
a=input("enter value-")
b=input("enter value-")
c=input("enter value-")
print(a,b)



# 2=compare 2 values dynamically from user and print the greater
if a>b:
    print(a, " is greater")
else:
    print(b, " is greater")


# 3=compare 3 values and print the greater one
if a>b:
    if a>c:
        print(a, "is greater")
    else:
        print(c, "is greater")
elif b>a:
    if b>c:
        print(b, " is greater")
    else:
        print(c,"is greater")

else:
    print(c, "is greater")

# 4=read the valure from user(0-8) and convert into word (in console alphabetically)

n=int(input("enter a number"))
if n in range(1,10):
    if n==0:
        print("ZERO")
    elif n==1:
        print("ONE")
    elif n==2:
        print("TWO")
    elif n==3:
        print("THREE")
    elif n==4:
        print("FOUR")
    elif n==5:
        print("FIVE")
    elif n==6:
        print("SIX")
    elif n==7:
        print("SEVEN")
    elif n==8:
        print("EIGHT")
    elif n==9:
        print("NINE")
else:
    print("enter proper number")


# 5=read the valure from user(0-8) and convert into word (in console alphabetically)
s=input("enter a string")
for i in range(0,len(s)):
    print(s[i], end=",")



# 6= Read name from user and print each character separately?
str = input("Enter some string with special characters, letters and numbers :")

print("alphabets are-")
for i in str:1
if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <=90):
        print(i, end = " ")

print("\n")
print("numbers are-")
for i in  str:
    if (ord(i) >= 48 and ord(i) <= 57):
        print(i, end=" ")

print("\n")
print("symbols are-")
for i in str:
     if (ord(i) >= 32 and ord(i) <= 47):  #or (ord(i) >= 58 and ord(i) <=64) or (ord(i) >= 91 & ord(i) <=96) or (ord(i) >= 123 & ord(i) <=126):
         print( i, end=" ")




# 7=wap to print emp details
def emp_details(empName,id,salary,mb_num,address):

    print("EMP Name-" ,empName , "\n" ,"id-" ,id, "\n", "Salary-" ,salary, "\n", 'phone num-' ,mb_num, "\n", "address-",address)

print("Employee_details", 1)
emp_details("SALONI",123,25000,7893981556,"BTM")
print()
print("Employee_details", 2)
emp_details("ANNAPURNA",124,26000,7894897988,"BTR")
print()
print("Employee_details", 3)
emp_details("ABHISHEK",125,27000,89535489189,"BBSR")
print()
print("Employee_details", 4)
emp_details("ANJUM",126,28000,7892146576,"MP")
print()
print("Employee_details", 5)
emp_details("AMITABH",127,29000,7892468468,"UP")



# 8=collect 2 emp details from user and compare their salary
l=[]
def emp_details(empName,id,salary,mb_num,address):
    print("EMP Name-" ,empName , "\n" ,"id-" ,id, "\n", "Salary-" ,salary, "\n", 'phone num-' ,mb_num, "\n", "address-",address)
    print("salary 1-" ,salary)
    l.append(salary)

print("Employee_details", 1)
emp_details("SALONI",123,25000,7893981556,"BTM")
print()
print("Employee_details", 2)
emp_details("ANNAPURNA",124,26000,7894897988,"BTR")
print(l)
if l[0]>l[1]:
    print(l[0],"is greater")
else:
    print(l[1], "is greater")


# 9=print charcter of a string
s="GOOGLE"
for i in range(0,len(s)):
    print(i+1," characher is-", s[i])


# 10=wap to print the num divisible by 5 from 1 to 50
for i in range(1,51):
    if (i%5==0):
        print(i,end=",")


# 11=wap to print the numbers which is divisible by 5,10,15 from range 200 to 999

for i in range(200,1000):
    if (i%5==0):
        if(i%10==0):
            if(i%15==0):
                print(i,end=",")

# 12=wap to swap 2 numbers
x,y=2,3
print("before swapping numbers are-" ,x,y)
x=x+y
y=x-y
x=x-y
print("after swapping numbers are-" ,x,y)

# 13=wap to reverse a number

n=int(input("enter a number-"))
rev=0
while  n>0:
    r=n%10
    rev = (rev * 10) + r
    n=n//10
print(rev)


# 14=wap to check the given string is pallindrome or not
s="afifa"
s1=s[::-1]
print(s)
print(s1)
if s==s1:
    print("string is pallindome")
else:
    print("string is not pallindome")


# 15=wap to calculate simple interest

p=int(input("enter the principal amount"))
t=int(input("enter the  year"))
r=int(input("enter the rateof interest"))
print("interest is-" ,(p*t*r)/100)

# 16=wap to merge 2 list and append the updated result in another list
l1=[15,"hi",58.35,'hello']
l2=[147,58,"bye",2.5]
l1.extend(l2)
l1.append("good")
l3=l1.copy()
print(l3)

# 17=wap to perform =-*/ in 1program
print(5+4)
print(5-4)
print(5*4)
print(5/4)  #1.25
print(10%3) #1
print("floor division-" ,20//8)  #2-round numbers
print(5**3) #125-power
print(2e2)  #200.0-exponetioal value
print(2*2**2) #8

# 18=wap to demonstrate all the dictionary methods in one program
d={'a':"TYSS",'b':"IBM",'c':"GOOGLE"}
print(d.keys())  #dict_keys(['a', 'b', 'c'])
print(d.values())   #dict_values(['TYSS', 'IBM', 'GOOGLE'])

d1=d.copy()
print(d1)  #{'a': 'TYSS', 'b': 'IBM', 'c': 'GOOGLE'}

d1.clear()
print(d1)    #{}
d.setdefault('d',"IBS")     #{'a': 'TYSS', 'b': 'IBM', 'c': 'GOOGLE', 'd': 'IBS'}
print(d)
d.pop('a')
print(d)   #{'b': 'IBM', 'c': 'GOOGLE', 'd': 'IBS'}

print(d.get('d'))  #IBS

# 19=count the no of vowels in a string
s="salonI"
l=[]

for i in range(0,len(s)):
    if s[i].__contains__("a") or s[i].__contains__("e") or s[i].__contains__("i") or s[i].__contains__("o") or s[i].__contains__("u") or s[i].__contains__("A") or s[i].__contains__("E") or s[i].__contains__("I") or s[i].__contains__("O") or s[i].__contains__("U"):
        l.append(s[i])

print("no of vowels-" ,len(l))



# 20=Swap 1st 2 elements with  last 2 elements inside a list
l=[1,"hi",14,5.36,10,"bye"]
print("before swaping" ,l)

size=len(l)
temp=l[0]
l[0]=l[size-1]
l[size-1]=temp

temp1=l[size-2]
l[size-2]=l[1]
l[1]=temp1

print("after swaping " ,l)