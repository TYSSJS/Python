#1read two values from the user and print in console
a=input("enter value for a:")
b=input("enter value for b:")
print(a,b)

#2compare two values which is greater
if(a>b):
    print("a is greater")
else:
    print("b is greater")

#3compare 3 values and print greater value
c=input("entera value for c:")
if(a>b and a>c):
    print("a is greater")
elif(b>c):
    print("b is greate")
else:
    print("c is greater")

#4read the input from he user in the range of 0-10 and output should be in respected words ex:1=one,2=two
num=input("enter a number: ")
if(num=='1'):
    print("ONE")
elif(num=='2'):
    print("TWO")
elif (num == '3'):
    print("Three")
elif(num=='4'):
    print("four")
elif (num == '5'):
    print("five")
elif (num == '6'):
    print("six")
elif (num == '7'):
    print("seven")
elif (num == '8'):
    print("eight")
elif (num == '9'):
    print("nine")
elif (num == '10'):
  print("Ten")
else:
    print("num is more than 10")

#5 read the user name from the user and print each charactor separately
s=input("enter a username")
i=0
while i < len(s):
    print (s[i])
    i+=1;

#6read th input from the user print each separatly:ex ad!@311 alpha:a,spl=!@,num=122
text=input("enter a text:  ")
i=0
u=[]
l=[]
N=[]
S=[]
while i < len(text):
 if(text[i]>'A' and text[i]<'Z'):
    u.append(text[i])

 elif(text[i]>'a' and text[i]<'z'):
    l.append(text[i])

 elif (text[i] > '0' and text[i] < '9'):
  N.append(text[i])

 else:
  S.append(text[i])

 i+=1;
print("capital are: ", u)
print("lowercase are:",l)
print("numbers are", N)
print("special charactors",S)


#7write a program to print employee deatails
for i in range(0,5):
    name=input("enter name:")
    id=input("enter id:")
    sal=input("enter salary:")
    designation=input("enter designation:" )
    print("NAME:",name, "ID:",id, "SALARY: ",sal, "Designation: ",designation)


#8string=GOOGLE print G O O G L E searately
p="GOOGLE"
i=0
while i < len(p):
    print (p[i])
    i+=1

#9 collect two employee deatails from the user and compare their salaries
name=input("enter name:")
id=input("enter id:")
sal=input("enter salary:")
designation=input("enter designation:" )
name1 = input("enter name:")
id1 = input("enter id:")
sal1 = input("enter salary:")
designation1 = input("enter designation:")
if sal>sal1:
    print(name," salary is more than",name1)
else:
 print( name1,"salary is more than ",name)

