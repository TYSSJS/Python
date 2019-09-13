# print("21th program")
#21 WAP to count the vowels from the string
string=input("Enter a String to count the vowels")
str=string.casefold()
print(str)
count=0
length=len(str)
for i in str:
       if(i=='a'or i=='o' or i=='i' or i=='u' or i=='e'):
           count=count+1
print("Number of vowels are: ",count)

# print("18th 19th 20th program")
# 18,19,20 WAP for expample in dictiionary,list and tuple
dic={'1':'emp1','2':'emp2','3':'emp3'}
list=list(input("enter 1a list").split())
tuple=(1,2,3,4,5)
print(list)
# print(dic)
print(tuple.count(2))
print(tuple.index(3))

list.append(4)
print(list)
print(list.pop(5))
# without args it will remove last digit
# print(list)
q=list.copy()
print(q)
q.clear()
print(q)

p=dic.copy()
print("copy of dictionary=",p)
print(dic.keys())
print(dic.values())

# 22 swap first 2 and last 2 elements inside the list
list=[10,20,30,40,50,60,70]
len=len(list)
list[0],list[-1]=list[-1],list[0]
list[1],list[-2]=list[-2],list[1]
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])

## print("7th program")
# 7 WAP to print employee details.
# empid,name,salary
def getempldetails(empid,name,salary,phoneno,address):
    print("Employee id= ",empid, "\n", "Salary",salary, "\n", "Phoneno",phoneno, "\n", "name",name ,"\n","address",address)

print()
print(" Employee_details-1")
getempldetails('Amr1233','anna',50000,8884843324,'Bangalore')

print()
print(" Employee_details-2")
getempldetails('Amr12453','radha',45000,8888743324,'Bangalore')

print()
print(" Employee_details-3")
getempldetails('Amr1278','rupa',57700,7884843324,'Bangalore')

print()
print(" Employee_details-4")
getempldetails('Amr1296','ruhi',57700,88848555324,'Bangalore')

print()
print(" Employee_details-5")
getempldetails('Amr1287','sudha',44000,7884843324,'Bangalore')
