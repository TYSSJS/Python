def add(a,b,c=None,d=None):
    if c!=None and d==None:
        print(a+b+c)
    elif c==None and d==None:
        print(a+b)
    else:
        print(a+b+c+d)

# method overloading
add(20,30)
add(100,200,300)


class a():
    def m1(self):
        print("from parent")
class b(a):
    def m1(self):
        print("from child")
o1=a().m1()
o2=b().m1() # method overriding