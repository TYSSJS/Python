# a= 12
# b= 13
# if a in range(1,20):
#     print(a)
# else:
#     print(b)
#
#
# a=input("Enter A ")
# b=input("Enter B ")
# if a>b:
#     print(a, "a is greater")
# else:
#     print(b, "b is greater")

# ladderif

# a=input("Enter A ")
# b=input("Enter B ")
# c=input("Enter C ")
# if a>b:
#     print("a is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")
#
# # nested if
# if a>b:
#     if(a>c):
#         print("a is greater")
#     else:
#         print("c is greater")
# elif b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# for i in range(0, 10):
#     if (i % 2 == 0):
#         continue
#     print(i)
# for i in range(0, 10):
#     if (i % 2 != 0):
#         continue
#     print(i)

def m1():
    pass
m1()


# no para no return
def m1():
    print("hi")
m1()


# para no return
def m1(a,b):
    print(a+b)
m1(10,20)


# para with return
def m1(a,b):
    return a+b
print(m1(10,20))


# no para with return
def m1():
    return "hi"
print(m1())