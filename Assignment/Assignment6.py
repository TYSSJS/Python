# 1.Using lamda and list comprehension perform any 5 programs.
# LAMBDA functions
# prg.1 # add 10 to the argument and print the result
x=lambda a:a+10
print(x(5))

# prg2. # multiplies argument with another args
x=lambda a,b:a*b
print(x(5,4))

# prg3. # sum of three numbers
x=lambda a,b,c:a*b*c
print(x(5,4,5))

# prg4. # write a method which return value using lambda
def m1(a,n):
   return lambda a,n:a*n
m1(2,2)

# 2.Bubble sort using python.
# def bubblesort(a):
#     n=len(a)
#     for i in range(n):
#         for j in range():
#             if a[j]>a[j+1]:
#                 a[j]=a[j+1]
#                 a[j+1]=a[j]
# a=12,1,5,10,9
# bubblesort(a)

# 3.Wap that displays which letters are present in both the strings. o/p: common characters
# str1="amrita"
# str2="ruhisarath"
# ls=list(set(str1)&set(str2)) #intersection of two strings to remove the duplicate and show only the common characters
# print("The common characters present in both the string:")
# for i in ls:
#     print(i)

# 4. WAP to read a text file and count the number of times a certain letter or word appears in the same file.
# e.g: the, is ,a--- occurrences
# input=input("Enter the letter or word")
# f=open("writefile.txt",'r')
# data=f.read()
# print(data.count(input))

# 5. WAP to append the content of one file to another file.
# append the writefile.txt to write1.txt
# f=open("writefile.txt",'r')
# data=f.read()
# f1=open("write1.txt",'w')
# f1.write(data)
# print(data)

# 6. WAP to read a file and count the no. of blank spaces in the text file
# f=open("Assignment6.txt",'r')
# data=f.read()
# print(data)
# count=0
# for a in data:
#     if(a.isspace()==True):
#         count+=1
# print("No. of blank spaces are=",count)


# 7. WAP to read a file and capitalize the first letter of each and every word in the file.
# f=open("Assignment6.txt",'w')
# data="I love python and python"
# f.write(data.title())