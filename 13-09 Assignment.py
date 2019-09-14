# 1. Illustrate Class
class one():
    print("hello")


obj = one()

# 2. even no. list comprehension
l = [1, 2, 3, 45, 56, 34, 98]
print([l[i] for i in range(0, len(l)) if l[i] % 2 == 0])

# 3.take input and show in form of dictionary
k1 = input("enter id")
v1 = input("enter id value")
k2 = input("enter name")
v2 = input("enter name value")

def dict(k1, v1, k2, v2):
    s = {k1: v1, k2: v2}
    print(s)
dict(k1, v1, k2, v2)

# 4. bank details
class bank():
    def details(self, acc, branch, name):
        self.Account = acc
        self.Branch = branch
        self.Name = name
        print("account- ", acc,"\n", "branch- ",branch,"\n", "name of branch- ",branch)
obj=bank()
obj.details(120831209, 'BTM', 'SBI')

# 5.credit debit
class bal:
     def add(self, balance, addamnt):
            print(balance+addamnt)
            return balance+addamnt
     def sub(self, tbal, deduct):
         print(tbal-deduct)

obj=bal()
balance = int(input("enter net balance"))
addv= int(input("enter add value"))
tbal=obj.add(balance, addv)
debtv= int(input("enter add value"))
obj.sub(tbal, debtv)

# 6.emp details
l=[]
class emp():
    def details(self, ename, acc, branch, name):
        self.Ename= ename
        self.Account = acc
        self.Branch = branch
        self.Name = name
        l=([("Ename- ", ename, "/n", "account- ", acc, "\n", "branch- ", branch, "\n", "name of branch- ", branch)])
        return l
obj=emp()
id1 = obj.details('annu', 120831209, 'BTM', 'SBI')
id2 = obj.details('affu', 120831208, 'BTR', 'ICC')
id3 = obj.details('salu', 120831207, 'BTH', 'AXIS')
id=input("enter id")
if id == 'id1':
    print(id1)
elif id == 'id2':
    print(id2)
else:
    print(id3)


# 7.tyss-welcome to tyss
s = {'tyss': 'welcome to tyss', 'ibm': 'welcome to ibm', 'ibs': 'welcome to ibs', 'hcl': 'welcome to hcl'}
i = input("enter the company")
if i in s:
    print(s.get(i))

# 8. assignment operator
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

# 9. add numbers
print('The sum is ', (int(input('Enter first number: '))+int(input('Enter second number: '))))

# 10.enter branch show name
l1=[]
l2=[]
d = {'annu': 'python', 'anjum': 'python', 'saloni': 'python', 'barish': 'python', 'mani': 'python', 'kimi':'java', 'dipu':'java', 'dipa':'java', 'ninja':'java', 'ben':'java'}
name=input("enter the name")
if name in d:
    print(d.get(name))
else:
    print("not a proper name")
# 12. sum of given number in list
l = []
i=0
for i in range(0, 5):
    i = int(input("enter a number"))
    l.append(i)
print(sum(l))

# 13.leap year
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

# 14. largest even no in list
l = [1, 2, 3, 45, 56, 34, 98]
k=[l[i] for i in range(0, len(l)) if l[i] % 2 == 0]
print(k)
print(k.sort())
print(k[-1])

# 15. strong number
num = int(input("enter a number"))
temp = num
sum = 0
while num:
    i = 1
    fact = 1
    d = num % 10
    while i <= d:
        fact = fact * i
        i = i+1
    sum += fact
    num = num//10
if temp == sum:
    print("strong number")
else:
    print("not a strong number")

# 16. count lower case
str = input("enter a string")
l=[]
for i in range(0 , len(str)):
    if ord(str[i])>= 97 and ord(str[i])<= 122:
        l.append(str[i])
print(len(l))

# 17.given key is present or not
d = {1: 'hii', 2: 'hello', 3: 'bye', 4: 'die'}
k = int(input("enter the key"))
print(d.keys())
if k in d.keys():
    print("key is present")
else:
    print("key is absent")

# 18.number not divisible by 2,3,7
print("numbers which are not divisible by 2,3,7 are: ")
for i in range(43, 959):
    if i % 2 != 0:
        if i % 3 != 0:
            if i % 7 != 0:
                print(i, end=" ")





