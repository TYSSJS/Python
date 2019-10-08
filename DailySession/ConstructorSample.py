# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#
#     def display(self):
#         print('''ID: %d\nName:%s'''%(self.id,self.name))
#
# emp=Employee('Amrita',1)
# emp.display()


# i=1;
# num = int(input("Enter a number:"));
# for i in range(1,11):
#     print("%d X %d = %d"%(num,i,num*i));

# n = int(input("Enter the number of rows you want to print?"))
# i,j=0,0
# for i in range(0,n):
#     print()
#     for j in range(0,i+1):
#         print("*",end="")

# list =[1,2,3,4]
# # count = 1;
# # for i in list:
# #     if i == 4:
# #         print("item matched")
# #         count = count + 1;
# #         break
# # print("found at",count,"location");
from filecmp import cmp

str='hello'
# num=5
# fl=5.6
# print("The string str : %s\nThe string num: %d\nThe float value is: %f"%((str),num,fl))
# print(str.capitalize())

li=[1,3,2,4,65,6,8,8]
l1=[54,545]
# del li[5]
# print(li)
# print((li * 2))
# print(li + l1)
# print(2 in li)
# print(len(li))
# print(len(str))

# l=[]
# n=int(input("Enter"))
# for i in range(n):
#     l.append(input("enter the value"))
# print(l)
# print(max(l))
# # print(cmp(l1, li))
# print(min(l1))
# print(l1.clear())
# l3=[]
# l3=l.copy()
# print(l3)
# l5=l.count('2')
# print("count",l5)
# l4=l1.extend(l)
# print(l4)
# try:
#     print("index",l.index('2'))
# except:
#     print("2 is missing")
# print("insert",l.insert(2,"done"))
# print(l)
# print(l.pop())
# try:
#     print(l.remove('4'))
# except:
#     print("value is missing")
# print(l.reverse())
# l6=l1.sort()
# print(l6)

# Employees=[(101,'dhanush',33),(102,'data',34),(103,'check','44')]
# for i in Employees:
#     print(i)


# s={1,2,3,4,5}
# print(s.update(8)  )
# print(s)
# s1={'emp1','emp2','emp3'}
# s2={'emp1','emp2'}
# print(s1.intersection(s2))
# s3={'emp1'}
# s4={'emp1','emp4','emp5'}
# print(s1.intersection_update(s2, s3,s4 ))
# print(s1)

# def invertlist(input_list):
#     return reversed(input_list)
#
# input_list=[1,2,3,4,5]
# out_list=[item for item in reversed(input_list)]
# print("output ",format(out_list))

# dic={'1':'value1','2':'value2'}
# dic1=dic.items()
# print(dic1)
# print(dic.setdefault('3', 'value3'))
# print(dic)
# print(dic.popitem())
# print(dic)
# print(dic.get('2'))

# custom iterator

# list = ['search', 'cart', 'orders', 'delivery to']
# li = iter(list)
# print(next(li))
# print(next(li))
# print(next(li))
# print(next(li))

set={1,2,5}
ll=list(set)
ll.sort(reverse=True)
print(ll)

str='fvdfdbg'
str=sorted(str)
print(str)