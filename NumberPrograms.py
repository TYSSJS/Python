"""#1 To print numbers divisible by 5,10,15 between 1-50
for num in range(1,50):
 if num%5==0 and num%10==0 and num%15==0:
    print(num)"""

"""#2 Print numbers divisible by 5,10,15 between 200-50
for num in range(200,999):
 if num%5==0 and num%10==0 and num%15==0:
    print(num,end=" ")"""

"""#3 Swap two numbers without temp
a=20
b=45
print("before swapping")
print(a,b)
a,b=b,a
print("after swapping")
print(a,b)"""

"""""#4Reverse the given number
num=int(input("Enter the number"))
rev=0
while(num!=0):
    rem=num % 10
    num=num // 10
    rev=rev*10+rem
print(rev)"""

"""#5 Number is Palidrome or not
num=int(input("Enter the number"))
rev=0
temp=num
while(num!=0):
    rem=num % 10
    num=num // 10
    rev=rev*10+rem
print(rev)
if(temp==rev):
    print("The given number is palindrome")
else:
    print("Not palidome")"""


"""#6 Calculate Simple Interest
P=int(input("Enter the principal amount"))
T=int(input("Enter the time units"))
R=int(input("Enter the rate of interest"))

SI=(P*T*R)/100
print(SI)"""

"""""#7To merge two List and append the updated in new list
l1=[1,43,'anusha']
l2=[2,4,19]
l1.extend(l2)
print(l1)
l3=l1
print("The updated new list :",l3)"""

"""# 8 Calculator Operations
def add(a,b):
    print(a+b)
add(2,4)

def sub(x,y):
    print(x-y)
sub(8,4)

def mul(a,b):
    print(a*b)
mul(2,4)

def div(a,b):
    print(a/b)
div(25,5)"""

# 9count the vowels in the given String
"""s=input("Enter the String")
length=len(s)
for i in range(1,length):
    if s[i] =='a'or s[i]=='e' or s[i]=='i'or s[i]=='o' or s[i]=='u':
       print(s[i],end=" ")
    else:
        print("the string does not hav vowels")"""

"""""#10 swap 1st and last two  in the list
l=[1,4,6,8,17,19]
print("The original list :",l)
l.reverse()
#print(l)
temp=l[0]
l[0]=l[1]
l[1]=temp
print("the swapped list :",l)"""

"""#11 Dictionary methods
d={'k1':'anusha','k2':'anvika','k3':'kamu'}
print(d)
print(d.keys())
print(d.values())
print(d.setdefault('k4'))
print(d.setdefault('k5','niceday'))
print(d)
c=d.copy()
print(c)
c.clear()
print(c)
print(d.get('k1'))"""

"""#12 Setmethods
s={1,4,99,2,1}
print(s)
s.add('hi')
print(s)
s.remove(2)
print(s)
s.pop()
print(s)
s.add('anvi')
print(s)
s.remove(4)
a=s.copy()
print(a)
a.clear()
print(a)

# to add another set with existing set
s1={2,66,23,'anu'}
s.update(s1)
print(s)

print("the new set values are :",s)"""

"""""#13 Tuple methods
t=[1,3,6,8,'anusha']
print(t.index(3))
print(t.count(6))
t.append(77)
print(t)
t.reverse()
print(t)
t1=[99.88,77]
t.extend(t1)
print(t)"""
































