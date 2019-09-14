# class Sample:
#     def __init__(self,name,add):
#         self.name=name
#         self.add=add
#     def display(self):
#         print(self.name,self.add)
#
# obj=Sample('abc','Mysore')
# obj.display()
#
# class Sample1:  #3 arguments
#     def __init__(self,name,add):
#         self.name=name
#         self.add=add
#     def display(self,mob_no):
#         print(self.name,self.add,mob_no)
#
# obj=Sample1('abc','Mysore')
# obj.display('1998')
#
# numbers=[1,2,3]
# sum=sum(numbers)
# print(sum)

s=int(input("enter how many  numbers :"))
l=[]
for i in range(s):
    n = int(input("enter the num t add :"))
    l.append(n)
    print(sum(l))

















