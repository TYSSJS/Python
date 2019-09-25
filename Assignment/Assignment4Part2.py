print("Program 10")
# 10. Take the input from the user for username and print the respective subject for that user.
username=input("Enter the user name")
dic={'Amrita':'Python','Anusha':'Python','Saritha':'Python','Shreyas':'Python','Lakshmi':'Python','Saritha':'JavaScript','Sulkshana':'JavaScript','Shailaja':'JavaScript','Neha':'JavaScript','Riya':'JavaScript'}
print(dic.get(username))

print("Program 13")
# 13.Read the input user in the format of list, and print the sum of the list.

list=list(input("enter 1a list").split(','))
l=len(list)
sum=0
for i in list:
 sum=sum+int(i)
print("Sum of all the elements present in the list is=",sum)

print("Program 14")
# 14. count the numeric digits in the string. e.g:'10A23fbgd45'...output:6 digits are present in the given input
str=input("Enter the value to count no. of digit")
# input=int(str)
count=0
for i in range(len(str)):
    if(str[i].isdigit()):
         count=count+1
print(count,"numeric digits are present in the given input")

print("Program 15")
#15 Write a program to find the leap year or not.
year=int(input("Enter an year"))
def leapYear(year):
    if(year % 4==0):
        if(year % 100==0):
            print(year,"is a leap year")
        else:
            print(year, "Not an leap year")
    else:
     print(year,"Not an leap year")
leapYear(year)

# print("Program 17")
#17 WAP to identify the strong number
num=int(input("Enter a number"))
sum=0
copy=num
while(num):
    fact=1
    i=1
    r=num%10
    while(i<=r):
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
print("Checking strong number")
if sum==copy:
    print("given number is strong number")
else:
    print("given number is not strong")

print("Program 18")
#18WAP to count the lowercase character in a given string
def Count(str):
# str=input("Enter the string")
    count=0
    for i in range(len(str)):
        if(str[i]>='a' or str[i]<='z'):
             count+=1
    print("lowercase letters:",count)

str='amritaLovesPython'
Count(str)

print("Program 16")
# 16 WAP to find the largest even no. in a list
list=int(input("Enter to what range u want to check the range"))
b=[]
c=[]
for i in range(0,list+1):
    if i%2==0:
        b.append(i)

    for i in range(43,958):
        if(i%2!=0 and i%3!=0 and i%7!=0):
            print(i,end=' ')
    else:
        c.append(i)
print("even numbers are=",b)
print("Largest even number is",b[-1])
print("odd numbers are=",c)

print("Program 19")
#19  WAP to check whether the given key present in a dictionary or not
check=input("Enter a key")
dic={'Amrita':'Python','Anusha':'Python','Saritha':'Python','Shreyas':'Python'}
if check in dic.keys():
    print("Key is present")
else:
    print("key is not present")


print("Program 20")
#20 WAP to display the numbers which is not divisible by 2,3,7 from the range 43 to 958
num=input("Enter a number")
def divisible():
    for i in range(43,958):
        if(i%2!=0 and i%3!=0 and i%7!=0):
            print(i,end=' ')
divisible()


