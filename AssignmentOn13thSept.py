#1=WAP to illustrate class
class Vehicle() :
    print("This is a vehicle class")
    def start(self):
        print("engine is starting")


obj = Vehicle()   # This is a vehicle class
obj.start()     # engine is starting

# 2=wap to display even numbers using list comprehension

print([i for i in range(31)  if i%2==0])   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# 3=take the input from user and display o/p in the form of dictionary
d ={}
for i in range(4):
    k = input("enter the key")
    v = input("enter the value")
    d.setdefault(k, v)
print(d)

# 4=wap to display bank details using class (bank name,user name,ac num,ifsc,branch name)

class Bank:
    def __init__(self,acntHolder_name,acc_num,bank_name,ifsc_code,branch_name):
        self.userName=acntHolder_name
        self.acc_no=acc_num
        self.bankName=bank_name
        self.ifscCode=ifsc_code
        self.branchName=branch_name
        print("user name is-",self.userName,"\n", "Account number-",self.acc_no, "\n", "bank name-",self.bankName,"\n",
              "IFSC code-" , self.ifscCode,"\n","branch name-", self.branchName)


print("BANK_DETAILS:")

obj=Bank("ANNAPURNA",354665656,"ICICI","IcIC12000","BANGLORE")


#5=wap to display the credited and debited bank amounts and balance as well

class bank_balance:
    balance=int(20000)
    print("Balance in the account-",balance)
    def credit_details(self):
        credit=int(input("enter the amount deposited-"))
        print("Balance credited is-",credit)
        total_balance=bank_balance.balance+credit
        # updated the bank main balance
        bank_balance.balance=total_balance
        print("Total balance after credit-",total_balance)


    def debit_details(self):
        debit = int(input("enter the amount debited-"))
        print("Balance debited is-", debit)
        total_balance=bank_balance.balance-debit
        bank_balance.balance=total_balance
        print("Total balance after dedit-", total_balance)
    print(balance)


obj = bank_balance()
obj.credit_details()
obj.debit_details()

# 6=take input from user (id), if it matches with id of the company, get the details

id = int(input("enter id-"))
if id == 1:
    def emp_1():
        print("emp_id:",id ,"\n" , "Name :" ,"Saloni", "\n", "Salary:" ,25000)
    emp_1()
elif id== 2:
    def emp_2():
        print("emp_id:",id ,"\n" , "Name :", "Annapurna", "\n", "Salary:" ,26000)
    emp_2()
elif id == 3:
    def emp_3():
        print("emp_id:", id, "\n", "Name :", "Narendra", "\n", "Salary:", 30000)
    emp_3()

elif id == 4:
    def emp_4():
        print("emp_id:", id, "\n", "Name :", "Nazma", "\n", "Salary:", 28000)
    emp_4()

elif id == 5:
    def emp_5():
        print("emp_id:", id, "\n", "Name :", "Abhi", "\n", "Salary:", 29000)
    emp_5()


# 7=take input from user if the name is equals to "anushree", print welcome to python
userName=input("Enter the user name-")
if userName == "Anushree":
    print("Welcome To Python")
else:
    print("Welcome To JavaScript")


# 8=write diff diff example for each assignment operator  ( += ,-+,*=,/=,%=)

a=50
a+=2
print(a)  #52
a-=2
print(a)  #50
a*=2
print(a)   #100
a/=25
print(a)   # 4.0
a %=10
print(a)   # 4.0

x =10
x ^= 2
print(x)  # 8

y =10
y <<=4
print(y) # 160

n = 15
n >>= 4
print(n)  # 0
print(" ")


# 9=wap to get summation of numbers upto a given range

rng=int(input("enter the range-"))
sum=0
for i in range(rng):
    sum=sum+i
print("summation of numbers in a given rannge is- ",sum,end=" ")
print(" ")



# 10=enter 10 name and display whether its in python or java script(5-py,5-jse)

name=input("Enter the name-")
record={"anu":"python", "manish":"javaScript", "abhi":"python" ,"saloni":"python", "praveen":"javaScript",
   "amit":"javaScript","anjum":"python", "akshya":"javaScript", "pavan":"python", "ritika":"javaScript"}

languageLearning= record.get(name)
print(name," is learning -",languageLearning)
print(" ")

# 13=read from user in the form of list and print the sum of list
list =[2,5,45,36,20,2.5,14,20.45]
print("the list is-",list)
s=0
for i in range(0,len(list)):
    s= s+ list[i]
print("sum of the elements in list without using inbuilt method-",s)
#  print("sum of the elements in the list using in built method-" ,sum(list[i] for i in range(0,len(list))))

print(" ")

# 14=wap to check the given year is leap yr or not

year=int(input("Enter the year-"))
if year%4 ==0:
    if year%4 ==0:
        if year%400 ==0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

print(" ")

# 15=wap to print largest even num in a given list
givenList=[25,21,12,47,10,98,24,57,69,66]
print(givenList)
evenList=[]

for i in range(len(givenList)):
     if ( givenList[i]%2 == 0):
         evenList.append(givenList[i])

evenList.sort()
print("all the even numbers in the list ", evenList)
print("largest even number in the list is- ", evenList[len(evenList)-1])
print("")


#  16=wap to print the to check whether the given num is strong or not  (1,2,145 are strong)

num=int(input("Enter a number to check it is strong num or not-:"))
temp = num
s = 0
while num > 0:
    i, fact = 1,1
    rem = num % 10
    while i <= rem:
        fact=fact*i
        i=i+1
    s = s+fact
    num //= 10
if s == temp:
    print("The number is a strong number")
else:
    print("The number is not a strong number")
print(" ")

# 17=wap to count the lower case char in a given string
str = input("Enter a string to count no of lower case characters-")
count = 0
listOfLowerCaseChar = []
for i in range(len(str)):
    if ord(str[i]) in range(97 , 123):             #ord(str[i]) >= 97 and ord(str[i]) <= 122:
        listOfLowerCaseChar.append(str[i])

print("no of lower case characters-" ,len(listOfLowerCaseChar))
print(" ")

# 18=wap to check whether given key is present in a dictionary or not

dict = {"name":"anu", "age":"24" ,"address":"Btm", "ph":"487852125525"}
print(dict)
key=input("Enter the key to check if its present in the above dictionary or not-")
if dict.__contains__(key):
    print(key, "is present in the dictionary as a key")
else:
    print(key, "is not present in the dictionary as a key")
print(" ")



# 19=wap to display the num which is not divisible by 2,3,7 from the range 43 to 958

print(" numbers which is not divisible by 2,3,7 from the range 43 to 958-")
for i in range(43,958):
    if i%2 !=0 and i%3 != 0 and i%7 != 0:
        print(i,end=" ,")



























