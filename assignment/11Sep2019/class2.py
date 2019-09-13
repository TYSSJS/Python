for i in range(10):
    print(i,end=' ')
    if i == 7:
        break
print(' ')
for i in range(15):
    if i%2!=0:
        continue
    print(i, end=' ')
print(' ')
def m1():
    pass

m1()

# we cannot have empty method & empty class
# something should be present inside method & class
# we can use pass

class c1:
    pass

# parameter & no return type
def m2(a, b):
    print(a+b)
    print("with parameters, no return type")


m2(6, 7)


def m3(a, b):
    print("with parameters & return type")
    return a+b


print(m3(5, 5))


def m4():
    return "hi"


print(m4())