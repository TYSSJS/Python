def add_number():
    print(1+2)
add_number()
#
def add_number(a,b):
    print(a+b)
add_number(1,2)
#
l=[4,5.4,6,8]
length=len(l)-1
for i in range(1,length):
    print(l[i],end=' ')
    #
for i in range(15):
    if(i%2!=0):
        continue
    print(i)
    # WAP to print empty method


def m1():
  print("No parameter and no return type")
m1()

def m2(a,q):
    print(a+q)
m2(1,2)

def m3(a,b):
    return a+b
print(m3(1,2))

def m4():
    return "hi"
print(m4())