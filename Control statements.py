#if else

i=2
if i in range(1,10):
    print(i,end=' ')
else:
    print("invalid")

print(' ')

if 100<20:
    print(20)
else:
    print(100)
print(' ')

#INPUT VALUES AT RUN TIME

a=input("enter value is a= ")
b=input("enter value is b= ")
if a<b:
    print(a," is smaller")
else:
    print(b," is smaller")


#elif

a=input("enter value is a= ")
b=input("enter value is b= ")
c=input("enter value is c= ")

if a<b:
    print(a," is smaller")
elif b<c:
    print(b," is smaller")
else:
    print(c," is smaller")