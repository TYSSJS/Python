# 1.Program to reverse a string without using list or concat
# str='amrita'
# len=len(str)
# rev=' '
# for i in range(0,len):
#     rev=str[i]+rev
# print(rev)

# reverse a number
# def numberRev():
#     num = 123456
#     num=num.__str__()
#     rev=''
#     print(num)
#     for i in range(0,len(num)):
#         rev=num[i]+rev
#     print(rev)
# numberRev()

# 2.Any program for list comprehension
# to print even numbers
# print([i*2 for i in range(1,11)])
# print([i for i in range(1,11) if i%2==0])

# 3.Wri te a program to print Fibonacci series
# print=0,1,1,2,3,5,8
# a=0
# b=1
# print(a,b,end=' ')
# for i in range(10):
#     c=a+b
#     print(c,end=' ')
#     a,b=b,c

# 4. Program to read a file and reverse each line
# instead of creating new file, here created using the write mode(auto generation of file)
# f=open("WRfile.txt",'w')
# for i in range(10):
#     data="Good morning"
#     f.write(data)
# print("writing")

# case1:to print the reverse order data from file
# f=open("WRfile.txt",'r')
# data=f.read()
# print(data,end='')
# f=open("reverse.txt",'w')
# rev=data[::-1]
# print(rev)

# case2:to print the data up and down
# for line in (list(open("WRfile.txt"))):
#     print("".join(reversed(line)))

    # case3:
# for line in (list(open("WRfile.txt"))):
#     print(line[::-1])

# 5. what is pylint?
# Pylint is a source-code, bug and quality checker for the Python programming language. It is named following a common convention in Python of a "py" prefix, and a nod to the C programming lint program.

# 6. Write git commands?
# Ans: Git clone<url> -b <branch name>
# Git status
# Git add *
# Git commit  –m  “commit message”
# Git remote add  origin<url>
# Git push –u origin <branch name>

# 7. Write a program to replace the specific words in a file?
# f=open("writefile.txt",'r')
# data=f.read()
# data=data.replace('morning','evening')
# f=open("writefile.txt",'w')
# f.write(data)
# data1='\n Good night \n'
# f.write(data1)
# print("writing")

#8. How to store dictionary values in a file?
# import json
# f=open("writefile.txt",'w')
# dic={"q1": "btm", "q2": "rajajinagar", "q3": "oldairport"}
# jsdata=json.dumps(dic)
# f.write(jsdata)
# print("success")

# 9.How to handle JSON file in that file, how you fetch only keys
# import json
# f=open("writefile.txt",'r')
# data=f.read()
# data=json.loads(data)
# print("data from the file: ",data)
# print("keys from the dictionary",dict(data).keys())

# 10 Write a Program for encapsulation?
# Encapsulation:you can restrict access to data from being modified and can only be modified when declared as '__'.
# and accessing by using getters and setters.
# Program1:-
# class PythonClass:
#     def __init__(self):
#         self.__version=22 #private always with __
#         self.a=22.5
#
#     def getVersion(self):
#         print(self.__version)
#
#     def setVersion(self,version):
#         self.__version=version
#
# obj=PythonClass()
# obj.getVersion()
# obj.setVersion(23)
# obj.getVersion()
# print(obj.a)
# Program 2
# class Employees:
#     def __init__(self):
#         self.name='Amrita'
#         self.empId='1ME08EC003'
#         self.__salary=10000
#
#     def getSalary(self):
#         print(self.__salary)
#
#     def setSalary(self,salary):
#         self.__salary=salary
#
# obj=Employees()
# obj.getSalary()
# obj.setSalary(20000)
# obj.getSalary()
# print("Employee "+ obj.name +" with "+obj.empId + " Salary "+"20000")

# 12 Write a basic program for iterator, decorator and generator
# decorators
# def outer(fn):
#     def inner():
#         print("inner of my method")
#         fn()
#         print("hi")
#         return inner
#
# @outer
# def Demo():
#     print("simple as it is")
#
# Demo()

# generators
# def genFact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#         yield f
#
# for i in genFact(5):
#     print(i)

# Iterator
# class Hotel:
#     def __init__(self):
#         self.menu=['idly','vada','dosa']
#         self.index=-1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index+=1
#         if self.index>=len(self.menu):
#             raise StopIteration
#         return self.menu[self.index]
#
# for i in Hotel():
#     print(i)

# sample()
# 13.Print the number from 1-6 using list comprehension
# print([i for i in range(1,7)])

# 15. Write a program to store the element present in list1 and not in list2
# list1=[1,6,7,8,5,5,5]
# list2=[2,3,8,5,6,2,8]
# list=[]
# list3=set(list1)
# list4=set(list2)
# print(list3)
# print(list4)
# print(list3.difference(list4))

# 17. Program to read a file and count occurrence of each word?
# from collections import Counter
# f=open("WRfile.txt",'r')
# words=f.read().lower().split()
# print(Counter(words))


# 18. To replace character of a string in other character?
# str='i love python'
# print(str.replace('i', 'u'))

# 19. How to get all the values in a dictionary?
# d={'k1':'value1','k2':'value2'}
# print(d.values())

# 20. To print missing letter in the list
# ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# l=['a','b','c','d','e','f','h']
# len=len(l)
# for i in range(0,len):
#     if (l[i]!=ch[i]):
#         break
# print("missing character is= ",ch[i])

# 21. Program to reverse list of string
# list=['apple','ball','cat']
# rev=list[::-1]
# print(rev)
# r,r1,r2='','',''
# lis1=[]
# data1=list[0]
# data2=list[1]
# data3=list[2]
# print(data1,data2,data3)
# for i in range(0,len(data1)):
#     r=data1[i]+r
# print(r)
# for j in range(0,len(data2)):
#     r1=data2[j]+r1
# print(r1)
# for i in range(0,len(data3)):
#     r2=data3[i]+r2
# print(r2)
# lis1.append(r)
# lis1.append(r1)
# lis1.append(r2)
# print(lis1)

# 22. Display names in alphabetical order?
# list=['sarath','amrita','saritha','lakshmi']
# list.sort()
# for i in list:
#     print(i)

# 23. Program for method overriding?
# class c1:
#     def m1(self):
#         print("method one")
#
#     def m1(self):
#         print("method two")
#
# obj=c1()
# obj.m1()

# 24. From a dictionary how to print key in one line and value in other line
# di={'k1':'v1','k2':'v2','k3':'v3','k4':'v4'}
# print(di.keys())
# print(di.values())

# 25. Write a method which can used as an alternative to string replace method
# str="I love python"
# l = str.split()
# print(l)
# l1 = []
# for i in l:
#     if i != "love":
#         l1.append(i)
#     else:
#         i = "hate"
#         l1.append(i)
# print(l1)

# 26(I) Replace every alternate character in a string with a “*” using inbuilt function and without using inbuilt function
# str='i love python'
# l=list(str)
# l1=[]
# for i in range(len(l)):
#     if i%2!=0:
#         l1.append(l[i])
#     else:
#         l[i]='*'
#         l1.append(l[i])
# print(l1)
# str1=''
# print(str1.join(l1))

# 26.(II)  l=[1,2,3,4,5], output = 5  create a list which will have the indexes of elements e.g. 1+4=5,2+3=5 so get the index of the elements which will give the output
# 	L=[(0,3),(1,2)]- number are index of that element
# list=[1,2,3,4]
# print([(i,j) for i in list for j in list if i+j==5])

# 27. Write a program for custom iterator
# class get_gen:
#     def __init__(self):
#         self.menu=['info','login','logout']
#         self.index=-1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index+=1
#         if self.index>=len(self.menu):
#             raise StopIteration
#         return self.menu[self.index]
#
# for i in get_gen():
#     print(i)

# 35. Write a code to remove the duplicate from a list.
# list=[1,1,2,2,3,3,4,5,6,7,8,9,9]
# list=set(list)
# print(list)

# 36. Write a code to count digits from a given number.
# str='123Wd45697'
# count=0
# num=' '
# len=len(str)
# for i in range(len):
#     if str[i].isdigit():
#         num=num+str[i]
#         count+=1
# print(count)

# 37. Write a code to reverse a string.
# str='amrita'
# len=len(str)
# rev=' '
# for i in range(0,len):
#     rev=str[i]+rev
# print(rev)

# 38. From a list copy all the even and odd numbers in separate lists in sorted order.
# lis=[42,12,55,77,79,22,22]
# l1=[i for i in lis if i%2==0]
# l2=[i for i in lis if i%2!=0]
# print("l1=",l1,'l2=',l2)
# l1.sort()
# l2.sort()
# print("l1=",l1,'l2=',l2)

# 34. Write a code to swap elements.
# a=1
# b=2
# a,b=b,a
# print('a=',a,'b=',b)

# 33. Write a code to sort elements present in list (without using built in method)
# lis=[5,4,6,7,2,5,4,8]
# case1
# lis2=['a','g','b','h']
# lis=set(lis)
# lis2=set(lis2)
# print(lis)
# print(lis2)
# case2
# lis=[5,8,6,7]
# len=len(lis)
# for i in range(len+1):
#     if(lis[i]>lis[i+1]):
#         lis[i],lis[i+1]=lis[i+1],lis[i]
#     print(lis)
# in this error is present

# 32. Write a program to fetch json data.
# import json
# f=open("jsonfile.txt",'r')
# data=f.read()
# jsondata=json.loads(data)
# print(jsondata)

# 31. How to get all the values in a dictionary program
# dict={'q1': 'btm', 'q2': 'rajajinagar', 'q3': 'oldairport'}
# print(dict.values())

# 29.Write a program, Given two strings, you have to insert second string exactly at the middle of the first string
# str1="amrita fine"
# str2="and geethu"
# len1=len(str1)
# print(str1[0:len1//2],str2,str1[len1//2:len1])
# print( "amrita {} fine.".format("and geethu"))



# 39. Write a code to return length of longest no. using list comprehension.json
# import json
# json.dict.values()

