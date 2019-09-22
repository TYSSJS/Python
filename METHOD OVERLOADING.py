#Method overloading  is not possible in python

# def add(a,b):
#     print(a+b)
#
# def add(a,b,c):
#     print(a+b+c)
#
#
# def add(a,b,c,d):
#     print(a+b+c+d)
#
# add(10,20)
# add(10,20,30)
# add(10,20,30,40)

#error --its not possible
#
# def add(a,b,c=None,d=None):
#     if c==None and d==None:
#         print(a+b)
#     elif c==None:
#         print(a+b+d)
#     elif d==None:
#         print(a+b+c)
#     else:
#         print(a+b+c+d)
#
# add(10,20)      #30
# add(10,20,30)   #60
# add(10,20,30,40)


def add(a,b,c=None,d=None):
    if c==None and d==None:
        print(a+b)
    elif c==None and d!=None:
        print(a+b+d)
    elif d==None and c!=None:
        print(a+b+c)
    else:
        print(a+b+c+d)

add(10,20)      #30
add(10,20,30)   #60
add(10,20,30,40) #100