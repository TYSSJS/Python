#wap which is divisible by 5 from 1 to 50
for i in range(1,50):
    if i%5==0:
        print(i,end=" ")
print(" ")

#write a program to which is divisible by 5 ,10, 15 from range 200-999
for i in range(200,999):
    if i%5==0 and i%10==0 and i%15==0:
        print(i,end=" ")

#wap to reverse a num
num=int(input("enter a num"))
temp=num
rev=0
while (num>0):
 d=num % 10
 rev=rev*10+d
 num=num//10
print(num)
print(temp)
if (temp==rev):
    print("numbers is aplindrome")
else:
    print("num is not palindrome")

#wap to check string is palindrome or not
str=input("enter a string")
def rev(s):
    s=s[::-1]
    return s
rev(str)
print("original string :",str)
print("revesr string is :",rev(str))

#wap to calculate simple interest
P=int(input("enter p:"))
T=int(input("enter t:"))
R=int(input("enter R:"))
SI=P*T*R/100
print(SI)

#wap to merge two list and appened that to one more list
l=[9,8,7]
print(l)
l1=[1,2,3]
print(l1)
l.extend(l1)
l3=l
print(l3)

#wap to perform to perform calculation operation
n1=(int)(input("enter a num1: "))
n2=(int)(input("enter num2: "))
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)


#count the no of vowels present in given string

string=input("Enter string:")
count=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count=count+1
print("Number of vowels are:")
print(count)

#wap to swap two numbers
a=1
b=2
a,b=b,a
print(b,a)
#swap first two with last two elements in a list
l=[1,2,3,4,5,6]
l[0],l[-1],l[1],l[-2]=l[-1],l[0],l[-2],l[1]
print(l)


