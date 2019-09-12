# anushree.p@testyantra.com
#2 Compare 2 values dynamically and which one is greater.
print("2nd program")
a=input("enter A")
b=input("enter B")
if a>b:
 print("A greater than B")
else:
 print("B greater than A")

print("3rd program")
#3 Compare 3 values and print which one is greater
a=input("enter A ")
b=input("enter B ")
c=input("enter C ")
if (a>b and a>c):
 print("A is greater")
elif (b>c and b>a):
 print("B is greater")
else:
    print("C is greater")

    print("4th program")
# 4 Read from input in the range of 0 to 9 and the expected output should be with respect words.
list=['zero','one','two','three','four','five','six','seven','eight','nine']
Input=input("Enter the number")
print(list[int(Input)])

print("5th program")
# 5Read the user name from the user and print each character seperately
Name=input("Enter the name")
length= len(Name)
for i in range(length):
    print(Name[i])

print("First program")
# 1 Read from the input and print in the console
a=input("Enter A")
b=input("Enter B")
print(a,b)

print("9th program")
# 9. Collect 2 emplyee details from the user and compare there salaries
emp1=input("Eneter emp name")
sal1=input("Enter the salary")
emp2=input("Eneter emp name")
sal2=input("Enter the salary")
if(sal1==sal2):
    print("Both employee have same salary")
else:
    print("Not matching salary")

print("10th program")
#10 Write a program to print the numbers which is divisible 5 from 1to 50
for i in range(1,50):
    if(i%5==0):
        print(i,"is divisible by 5")

print("6th program")
# 6 Read the input from the user, and seperate the seperate special character, alphabet, digits
str='$12ABC3_'
num=''
special=''
alpha=''
length=len(str)
for i in range(length):
      if(str[i].isdigit()):
          num=num+str[i]

      elif(str[i]>='A'and str[i]<'Z') or(str[i]>='a' and str[i]<='z'):
          alpha=alpha+str[i]

      else:
          special=special+str[i]
print("Special character are=",special)
print("Number is=",num)
print("Alphabet is=", alpha)

print("8th program")
# 8. Name="Google" Print"first character:G"
name=input("Enter Google")
length=len(name)
for i in range(length):
    print(i+1,"character is",name[i])

print("11th program")
#11 Write a program which is divisible by 5,10,15 from the range 200 to 999
for i in range(200,999):
    if(i%5==0 and i%10==0 and i%15==0):
        print(i,end=' ')


print("12th program")
#12 SWAP to swap two nos
a,b=1,2
a,b=b,a
print(a)
print(b)

print("13th program")
#13 WAP to reverse a number
num='456'
rev=' '
for i in range(len(num),0,-1):
    rev=rev+num[i-1]
print(rev)

print("14th program")
#14 WAP to reverse a number
str='malayalam'
rev=' '
for i in range(len(str),0,-1):
    rev=rev+str[i-1]
print(rev)
if(str==rev):
    print("String is a palindrome")
else:
    print("String is not a palindrome")

print("15th program")
#15 WAP to claculate Simple interest
pAmt=10000
r=0.05
t=2
num=pAmt*r*t
SI=num/100
print(SI)

print("16th program")
#16 Write a program to merge two list and append the updated result in one more list
l=[1,2,3,4,5]
l1=[7,8,9]
l.extend("list after merging=",l1)
print(l)
l2=l.copy()
print("list after updating to another list=",l2)

print("17th program")
#17 WAP to perform the calculator operator in one program such as Add,mul,sub,division
num1=input("enter a number")
num2=input("enter another number")
a=int(num1)
b=int(num2)
print("Addition=",(a+b))
print("Substraction=",(a-b))
print("Multiplication=",(a*b))
print("Division=",(a/b))





