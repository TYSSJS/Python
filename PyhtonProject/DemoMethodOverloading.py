# def add(a,b):
#     print(a+b)

#method overloading is not possible in python
# def add(a+b+c):
#     print(a+b+c)

def add(a,b, c=None, d=None):
    if c == None and d == None:
        print(a+b)
    elif c==None and d!= None:
        print(a+b+d)
    elif c!= None and d== None:
        print(a+b+c)
    else:
        print(a+b+c+d)
add(1,2)
add(1,2,3)
add(1,2,3,4)

