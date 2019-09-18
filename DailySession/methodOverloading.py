# def add(a,b):
#     print(a+b)
# def add(a,b,c):
#     print(a+b+c)
# def add(a,b,c,d):
#     print(a+b+c+d)
# add(1,2) #this will throw error
# Since in python, method overloading is not possible.
# we can overcome it with declaring the variable to none, as done below
# Traceback (most recent call last):
#   File "C:/Users/Amritha/PycharmProjects/PythonProject/methodOverloading.py", line 7, in <module>
#     add(1,2)
# TypeError: add() missing 2 required positional arguments: 'c' and 'd'

def add(a,b,c=None,d=None):
    if c==None and d==None:
        print(a+b)
    elif c==None and d!=None:
        print(a+b+d)
    elif c!=None and d==None:
        print(a+b+c)
    else:
        print(a+b+c+d)
add(1,2)
add(1,2,3)
add(1,2,3,4)