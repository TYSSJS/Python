a=10
b=20
print("a={0},b={1}".format(a,b))

c=1234
print("a={0},b={1},c={2}".format(a,b,c))

def add(a,b):
    return a+b
a=int(input("a"))
b=int(input("b"))
print(add(a,b))

#lambda peration +
sum=lambda a,b:a+b
print(sum(1,3))

#lambda peration +
sum=lambda a,b:a+b
print(sum(1,3))
print(sum(10,30))

#lambda peration -
sub=lambda a,b:a-b
print(sub(1,3))
print(sub(10,30))

#lambda peration +
mult=lambda a,b:a*b
print(mult(1,3))

#lambda peration +
div=lambda a,b:a/b
print(div(1,3))