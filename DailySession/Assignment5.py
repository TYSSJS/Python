# # File Handling Question
# print("Question no. 9")
# # 9. Read a file and print the data in console
# f=open('file1.txt','r')
# data=f.read()
# print("Successfully reading data: ",data)
#
# print("Question no. 10")
# # 10. Write the data to the existing file that should contain some characters.
# f=open('writefile.txt','w')
# data='Good Afternoon'
# f.write(data)
# data1='\n how r u \n reading python '
# data2='get the data from python class'
# f.writelines(data1)
# f.write(data1)
# f.write(data2)
# print("Success")
# # writefile.txt will be created
#
# print("Question no. 11")
# # 11.Read the data from the file and print only 7line of that file.
# f=open('writefile.txt','r')
# for i in range(7):
#     data=f.readline()
#     print(data,end=' ')

# print("Question no. 12")
# # 12.WAP to count how many words in that file.
f=open('writefile.txt','r')
line=0
characters=0
for i in f:
    characters=characters+len(i)
print(characters)
print(line)

# print("Question no. 13")
# # 13. WAP to print first character of that file
# f=open('file1.txt','r')
# data=f.readline(1)
# print("Read first character of the file1.txt : ",data)

# print("Question no. 14")
# 14. WAP to count the unique words in the file(remove duplicate)
# f=open('writefile.txt','r')
# data=f.read()
# list=data.split()
# print(list)
# s=set(list)
# print(s)
# it removes the duplicates

# print("Question no. 15")
#15 WAP to print the file in the reverse order.
# def revFile():
#     f=open("writefile.txt",'r')
#     value=f.read()
#     f1=open("reverse.txt",'w')
#     data=value[::-1]
#     f1.write(data)
#     print(data)
# revFile()
# print("Question no. 16")
# #16. create one file perform addition,mul,subs,division and that method in one more file using import.
from PythonPack import Assignment5Question16 as a

# not clear
# class Fibonacci(object):
#     def __init__(self, limit):
#         self.limit = limit
#         self.count = 0
#         self.values = []
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.count += 1
#         if self.count > self.limit:
#             raise StopIteration
#
#         if len(self.values) < 2:
#             self.values.append(1)
#         else:
#             self.values = [self.values[-1], self.values[-1] + self.values[-2]]
#         return self.values[-1]






