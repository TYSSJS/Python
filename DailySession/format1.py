# FORMAT FUNCTION
a=12
b=123
print("a={0}, b={1}".format(a,b))
# instead of writing below codes we can call "format funtion" for the large number of data
# print("a and b=",a,b)
# print("a=",a,"b=",b)

# WAP to add two numbers using methods
# case1:
# c=0
# def add():
#     a=int(input("Enter a number"))
#     b=int(input("enter a number"))
#     c=a+b
#     print(c)
# add()

# case2:
# def sum(a,b):
#     return a+b
# print(sum(1,3))

# case3: lambda is a function we are giving 2variables
'''sum=lambda a,b :a+b
print(sum(1,2))
print(sum(2,3))'''

# WAP to print only the even numbers from the list
# case1:
l=[7,5,6,3,2,4]
for i in range(len(l)):
    if(i%2==0):
        print(i,end=' ')

#case2 using lambda function
l=[1,2,3,5,6,89,23,7,4,4,8]
l2=list(filter(lambda l:l%2==0,l))
print(" ")
print(l2)
# print(even(l[2]),l[2])
