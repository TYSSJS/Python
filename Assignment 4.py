#1. wap to illustrate a class
class Demo1:

    def display(self):
        print("displaying")

#2.wap to display even numbers using list comprehension
l=[2,6,8,9,5,7]
print([l[i] for i in range(0,len(l))  if(l[i]%2==0)])
print([i*2 for i in range(1,8)])  #6 it will give count of 5 even numbers i.e from [2,4,6,8,10]

#3.take input from user and display o/p in the form of dictionary
key1 = input("enter the id : ")
value1 = input("enter the value: ")
key2=input("enter the key2: ")
value2=input("enter the value2 : ")

def keyvalue(key1,value1,key2,value2):
        dictionary={key1:value1,key2:value2}
        print(dictionary)

keyvalue(key1,value1,key2,value2)

#4-bank details
class Bank():
    def __init__(self,accno,ifsc,bname,addr,amount):
        self.accontno=accno
        self.ifsccode=ifsc
        self.branchname=bname
        self.address=addr
        self.amount=amount

    def display(self):
        print('Account number is',self.accontno,' IFSC code is',self.ifsccode,'Branch name is',self.branchname,' Address is',self.address,'Bank balance is',self.amount)
obj=Bank('CNB9603','IFSC0000155','Basavangudi','Bangalore',"Rs.50,000")
obj.display()

#5-credit and debit
class BankTransaction():

  def credit(self,bal,camount):
      print(bal+camount)
      return bal+camount

  def debit(self,bal,damount):
      print(bal-damount)
      return bal-damount

obj=BankTransaction()
bal=int(input("Enter the balance : "))
camount=int(input("Enter the amount to be credited : "))
damount = int(input('Enter the amount to be debited : '))
print("Balance after credit is " )
obj.credit(bal,camount)
print('Balance after debit is ')
obj.debit(bal,damount)


#6-take user input and fetch all details using empid
class Empd():
    def emp_det(self,eid,ename,edept):
        self.eid=eid
        self.ename=ename
        self.edept=edept

dic={'id1':['shreyas','EC'],  'id2':['Gautham','IS'], 'id3':['Manju','Mech']  }

key=input(" Please enter the key ")
if key in dic:
    print(dic.get(key))
else:
    print('User not found!')

obj=Empd()
obj.emp_det('eid','ename','edept')

#7-take user i/p if c.name='TYSS' print the foll statement
d={'TYSS': 'Welcome to python', 'MicroFocus':'Welcome to MicroFocus', 'SJS':'Welcome to SJS'}

i = input("Please enter the company name :")
if i in d:
    print(d.get(i))
else:
    print("Sorry, Company not found ")

#8- example for assignment operatory
a=90
b=70
c=3
d=2
a-=b
print(a)
a*=b
print(a)
a//=b
print(a)
a+=b
print(a)
c**=d
print(c)
ce=d
print(c)

#9-calculate summation
print("sum is", int(input("enter the 1st number to add: "))+ int(input("enter the 2nd no: ")))

#10-enter the name branch should be displayed
d={'shreyas':'python','santhosh':'python','denver':'python','professor':'python','tokiyo':'python','raqual':'js','sudeep':'js','upendra':'js','darshan':'js','muruli':'js'}
name=input("Please enter the name to get the branch :")
if name in d:
    print(d.get(name))
else:
    print("Please enter a proper name")

#13- read input from user and print the sum of list

row = int(input("enter how many  numbers :"))
l=[]
for i in range(row):
    n = int(input("Enter the numbers to add :"))
    l.append(n)
    print(sum(l))

#14 no of digits in string
str='430bcid19603'
count=0
for i in str:
    if(i.isdigit()):
        count = count+1
print("no of digits is: ", count)

#15 iven year is leap or not
year=int(input("Enter a year : "))

if(year%4==0):
    print("leap year ")
elif(year%100==0):
    print("leap year ")
elif(year%400==0):
    print("leap year ")
else:
    print("not a leap year")

# #16 largest even no
l=[4,2,6,18,20]
z=[l[i] for i in range(0,len(l)) if l[i]%2==0]
print(z)
z.sort()
print(z)
print(z[-1])

#17 check strong or not
sum = 0
num = int(input("enter the number: "))
temp = num
while(temp>0):
    digit = temp%10
    fact = 1
    while(digit >= 1):
        fact = fact*digit
        digit = digit-1
    sum = sum+fact
    temp = temp//10
if(sum == num):
    print("strong number")
else:
    print("Not a strong number")

#18-count lowercase char in a given string
st=input("Enter a string :")
count = 0
for i in st:
    if(i.islower()):
        count = count+1
print("no of lower case letters are :",count)

#19-check given key is preset in dictionary or not
d={'1':'denver', '2':'professor', '3':'tokiyo', '4':'shreyas'}

key = input("Enter the key to search")
if key in d.keys():
    print("Key is present & the value of key is :")
    print(d[key])
else:
    print("key is not present")

#20- print no's not divisible by 2,3,7 b/n range 43-958
l=[]
count=0
for i in range(43,959):
    if (i%2!=0):
        if(i%3!=0):
            if(i%7!=0):
                l.append(i)
                count = count + 1
                #print(count)
                print(i,end=' ')


