#  2=wap for each and every type of inheritance
# #SINGELEVEL INHERITANCE:-
# class super:
#     print("this is a super class")
#
#
# class sub(super):
#     print("this is a sub class")
#
# obj=sub()
#
# #MULTILEVEL IN HERITANCE:-
# class super1:
#     def m1(self):
#         print("1st super class")
#
# class super2(super1):
#     def m2(self):
#         print("2nd super class")
#
# class sub(super2):
#     def m3(self):
#         print("it is a sub class")
#
# obj=sub()
# obj.m3()
# obj.m2()
# obj.m1()
#
# # Hierarchical inheritance:-
# class parent():
#     def m1(self):
#         print("grand parent class")
#
# class sub1(parent):
#     def m2(self):
#         print("1st sub class")
#
# class sub2(parent):
#     def m3(self):
#         print("2nd sub class")
#
# obj=sub2()
# obj.m1()
# obj.m3()
# obj=sub1()
# obj.m1()
# obj.m2()

# # MULTIPLE INHERITANCE:- if here m and m1 are of same name then it will override the 1st method
# class p():
#     def m1(self):
#         print("m in p class")
#
# class p1():
#     def m1(self):
#         print("m1 in p1 class")
#
#
# class p2(p,p1):
#     def m2(self):
#         print("multiple inheritance")
#
# obj=p2()
# obj.m2()
# obj.m1()

# #HYBRID INHERITANCE
# class c1():
#     def m1(self):
#         print("Hybrid-main super class")
#
# class c2(c1):
#     def m2(self):
#         print("1sub sub class")
#
# class c3(c1):
#     def m3(self):
#         print(" 2nd sub class")
# class c4(c2,c3):
#     def m4(self):
#         print("sub class")
#
# obj=c4()
# obj.m1()
# obj.m2()
# obj.m3()
# obj.m4()


#  4=how u will perform method over loading and overriding with examples
# METHOD OVERLOADING
# def add(a,b,c=None,d=None):
#     if c==None and d==None:
#         print(a+b)
#     elif c==None and d!=None:
#         print(a+b+d)
#     elif d==None and c!=None:
#         print(a+b+c)
#     else:
#         print(a+b+c+d)
#
# add(10,20)      #30
# add(10,20,30)   #60
# add(10,20,30,40) #100

#METHOD OVERRIDING
# class p():
#     def m1(self):
#         print("m in p class")
#
# class p1():
#     def m1(self):
#         print("m1 in p1 class")
#
#
# class p2(p,p1):
#     def m2(self):
#         print("multiple inheritance")
#
# obj=p2()
# obj.m2()
# obj.m1()

## 5=wap to perform squareroot of a given number
# import math as m
# num=int(input("enter the number of which you want to get sqrt-"))
# print(m.sqrt(num))

## 6=wap to perform fibonacci series in 2 diff ways

# WAY-1
# x,y = 0,1
# num=int(input("enter the range of fibonacci series-"))
#
# while y < num:
#     print(y,end=",")
#     x, y = y, x+y



# #7=generate a random numbers from d range 0 to 9 , o/p only 1 num
# import random as r
# for i in range(1):
#     print(r.randint(0,10))



# # 8=generate 10 different numbers using library or modules
# import random
# def ph():
#     n='0000000000'
#     while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
#         n=str(random.randint(10**9,10**10-1))
#         return  n[:3] + '-' + n[3:6]+ '-' + n[6:]
#
# for i in range(11):
#     print(ph())


# import random
# print("Printing mobile number-")
# for i in range(1,11):
#     for j in range(0,10):
#         print(random.randrange(0,9,1),end=" ")
#     print(" ")



# #9= wap to read a file and print data in console
#
# f2=open("file.txt","w")
# f2.write("good morning")
# f2.close()
# f1=open("file.txt","r")
# print(f1.read())

# 10=write the data to the existing file
# f=open("file.txt","a+")
# f.write(" dear friend \n Very good morning \n How are you? \n i am fine and you? \n i am also fine \n  What are you doing now? \n  I am working as an Software Engr in TYSS \n Nice to meet you \n Have a good day")


# 11=read the data from the file and print only 7 lines of the file

# f1=open("file.txt","r")
# lines=f1.readlines()
# print(lines[6])

# 12=wap to count how many words,Characters and lines in that file
#
# file=open("file.txt","r")
# lines=0
# words=0
# chars=0
# for line in file:
#     wordsList = line.split(" ")
#     lines = lines + 1
#     words = words + len(wordsList)
#     chars = chars + len(line)
# print("No of lines in the file-", lines)
# print("No of words in the file is-", words)
# print("No of characters in the file-", chars)

# 13=wap to print 1st character of that file
# f=open("file.txt","r")
# print("First character of the file is-", f.readline(1))

# 14=wap to count the unique words in that file
# file=open("file.txt","r")
# word={" "}
# for line in file:
#     wordsList = line.split(" ")
#     for i in wordsList:
#         word.add(i)
#
# print("num of unique words in the file is -", len(word))

# file=open("file.txt","r").read()
# print(set(file.split()))


# 15=wap to print the file in the reverse order

file=open("file.txt","r")
for line in reversed(list(file)):
    print(line.rstrip())




