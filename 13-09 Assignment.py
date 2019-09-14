#1-illustrate a class
class one():
    name='xyz'
    def display(self):
        print("displaying")
#2-even no using list comprehension
l=[2,6,8,9,5,7]
print([l[i] for i in range(0,len(l))  if(l[i]%2==0)])
#or
#print([i*2 for i in range(1,6)])  #6 it will give count of 5 even numbers i.e from [2,4,6,8,10]

#3-take input from user and display o/p in the form of dictionary
key1=int(input("enter the id"))
value1=int(input("enter the value"))
key2=input("enter the key2")
value2=input("enter the value2")
def keyvalue(key1,value1,key2,value2):
        set={key1:value1,key2:value2}
        print(set)
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
        print(self.accontno,self.ifsccode,self.branchname,self.address,self.amount)
obj=Bank('25','Ab12','Btr','bang',1000)
obj.display()

#5-credit and debit
class Bankcd():
  def credit(self,bal,addamnt):
      print(bal+addamnt)
      return bal+addamnt
  def debit(self,totaldeb,subamnt):
      print(totaldebit-subamnt)
      return totaldebit-subamnt
obj=Bankcd()
bal=int(input("enter the balance"))
addamnt=int(input("enter the amoun to be added"))
totaldebit=obj.credit(bal,addamnt)
obj.debit(totaldebit,addamnt)

#6-take user input and fetch all details using empid
class Empd():
    def emp_det(self,eid,ename,edept):
        self.eid=eid
        self.ename=ename
        self.edept=edept
d={
    'id1':['afifa','AT'],
    'id2':['saloni','MT'],
    'id3':['annu','dev']
   }
key=input("enter the key")
if key in d:
    print(d.get(key))

obj=Empd()
obj.emp_det('eid','ename','edept')

#7-take user i/p if c.name='TYSS' print the foll statement
d={'TYSS':'Welcome to python','SONY':'wel to sony','XILINX':'wel to xilinx'}
i=input("enter the cname")
if i in d:
    print(d.get(i))
else:
    print("nothing")
#or
# class Company():
#     def comName(self):
#         cname = input("enter the company name")
#         if(cname=='TYSS'):
#             print("Welcome to python")
# obj=Company()
# obj.comName()

#8- example for assignment operatory
a=90
b=70
c=3
d=2
a-=b  #a=a-b
print(a)
a*=b  #a=a*b
print(a)
a//=b  #a=a//b
print(a)
a+=b  #a=a+b
print(a)
c**=d  #c=c**d
print(c)
ce=d  #c=ced
print(c)

#9-calculate summation
print("sum is", int(input("enter the 1st number to add: "))+ int(input("enter the 2nd no: ")))

#10-enter the name branch should be displayed
l=[]
d={'afi':'python','saloni':'python','anu':'python','abhi bhai':'python','pavan bahi':'python','mani bhai':'js','praveen':'js','amit':'js','pagal':'js','abc':'js'}
name=input("enter the name to get the branch")
if name in d:
    print(d.get(name))
else:
    print("not a proper name")

#13- read input from user and print the sum of list

s=int(input("enter how many  numbers :"))
l=[]
for i in range(s):
    n = int(input("enter the num t add :"))
    l.append(n)
    print(sum(l))
#or
# s1=input("enter elements to be separated by space")
# list=s1.split()
# print("find the sum of numbers")
# sum=0
# l=[]
# for i in list:
#     sum+=int (i)
# l.append(sum)
# print("sum is : ",l)

#or
# l=[]
# i=0
# for i in range(0,5):
#     i=int(input("enter the no"))
#     l.append(i)
# print(sum(l))

#14 no of digits in string
str='10a1b2c345'
count=0
for i in str:
    if(i.isdigit()):
        count=count+1
print("no of digit is: ",count)

#15 iven year is leap or not
year=int(input("enter a year : "))
if(year%4==0):
    print("leap year ")
elif(year%100==0):
    print("leap year ")
elif(year%400==0):
    print("leap year ")
else:
    print("not a leap year")

#16 largest even no
l=[4,2,6,18,20]
z=[l[i] for i in range(0,len(l)) if l[i]%2==0]
print(z)
z.sort()
print(z)
print(z[-1])

#or
# num=int(input("enter the no of elements to add : "))
# l=[]
# for i in range(0,num):
#     ele=int(input("elements are : "))
#     l.append(ele)
# l2=[]
# for i in  l:
#     if(i%2==0):
#         l2.append(i)
# l2.sort()
# count=0
# for i in l2:
#     count=count+1
# print("largest even no is : ",l2[count-1])

#17 check strong or not
sum=0
num=int(input("enter the number: "))
temp=num
while(temp>0):
    digit=temp%10
    fact=1
    while(digit>=1):
        fact=fact*digit
        digit=digit-1
    sum=sum+fact
    temp=temp//10
if(sum==num):
    print("strong no")
else:
    print("not a strong no")

#18-count lowercase char in a given string
st=input("Enter  string")
count=0
for i in st:
    if(i.islower()):
        count=count+1
print("no of lower case letters are :",count)

#19-check given key is preset in dictionary or not
d={'1':'abc','2':'xyz','3':'jimmy','4':'shergill'}
key=input("enter the key to find")
if key in d.keys():
    print("key is present and the value of key is :")
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
                print(count)
                print(i,end=' ')
































