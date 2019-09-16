
#1. Write a simple program to illustrate class
print("Program1")
class Simple():
    a=10
    def simplemethod(self):
        print("This is simple python class")
obj=Simple()
print(obj.a)
obj.simplemethod()

# 2. WAP to display even numbers using LIST Comprehension
print("Program 2")
print(list(i*2 for i in range(1,10)))

#9 Summation of given no. e.g:,summation of 3=3+2+1
print("Program 9")
user=input("Enter a number")
num=int(user)
sum=0
for i in range(num+1):
    sum=sum+i
print(sum)

# 3.Take the input from the user and display the dictionary format
print("Program 3")
dic=dict()
user_input=input("Enter key and value")
key,value=user_input.split(",")
dic[key]=value
print(dic)

# 4. WAP to display bank details using class(data from user and display)
print("Program 4")
class Bank():
    def __init__(self,Cname,Anumber,Idproof):
        self.nm=Cname
        self.acc=Anumber
        self.id=Idproof
    def displayBankdetails(self,custNo):
        print("-----------BANK DETAILS----------")
        print("CustomerName:",self.nm,"\n","AccountNumber:",self.acc,"\n","Idproof:",self.id,"\n","Customer number:",custNo)

obj=Bank('Amrita',789756,'Aadhaarcard')
obj.displayBankdetails('123456')

# 5 WAP to credit and debit balance of a colour
print("Program 5")
creditAmt=int(input("Enter the amount to be credited"))
def credit(amount):
    amount = 40000
    amount=amount+creditAmt
    print("credited final amount= ", amount)
credit(creditAmt)
debitAmt=int(input("Enter the amount to be debited"))
def debit(amount):
    amount = 40000
    amount=amount-debitAmt
    print("debited final amount= ",amount)
debit(debitAmt)

#6. Take the input from the user 5 employee details .And write the employee details, whenever id will be given.
class Employee():
    def __init__(self,EmpID,EmpName,EmpPhoneNo,EmpSalary,EmpAddress):
        self.Id=EmpID
        self.Name=EmpName
        self.PhoneNo=EmpPhoneNo
        self.Salary=EmpSalary
        self.Address=EmpAddress
    def getEmployeeDetails(self):
        l=[self.Name, self.PhoneNo, self.Salary,self.Address]
        d.setdefault(self.Id,l)

print("--EMPLOYEE DETAILS--")
d={}
no_of_users=int(input("Enter the number of users"))
for i in range(0,no_of_users):
    EmpId=input("Enter the Employee id")
    EmpName=input("Enter the Employee name")
    EmpPhoneNo=input("Enter the Employee phone number")
    EmpSalary=input("Enter the Employee Salary")
    EmpAddress=input("Enter the Employee address")
obj=Employee(EmpId,EmpName,EmpPhoneNo,EmpSalary,EmpAddress)
obj.getEmployeeDetails()
keyinput=input("Enter the key")
d.get(keyinput)
print(d)

# 7.Name TYSS in console and must print "welcome to python", company name can be anything should print nothing
class CompanyName():
    def checkCompanyName(self):
        company=input("Enter the name of the company")
        if(company=='TYSS'):
            print("Welcome to Python")
        else:
            print(" ")
obj=CompanyName()
obj.checkCompanyName()


# 8.Write different examples of assignment operator +=,-=,*=
b=0
b-=10
print("Subtraction",b)

a=10
a+=10
print("Add assignment operator",a)

a*=10
print("Multiplication ",a)

a/=10
print("Division",a)

c=2
c%=a
print("modulus",c)

c=5
c^=3
print("not of",c)

d=9
d//=5
print("floor division=",d)
# floor division will remove digits after the decimal
# 9/5=1.8=1

print("Exponential of",5e2)

x=2
x<<=3
print("left shift",x)

x=2
x>>=1
print("Right shift",x)
