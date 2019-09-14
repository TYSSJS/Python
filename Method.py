# method declaration:
# 1
def add():
    print("addition of 1 and 2 is-" ,1+2)
add()

# 2

a=12
b=15
def add(a1,b1):
    print(a1+b1)
add(a,b)


# 3
def main():
    pass

# 4
def main1(a,b,c):
    return (a+b+c)
print(main1(10,20,30))


# 5
def main():
    print("no return type no parameters")
main()


# 6
def main():
    return  "hi"
print(main())



for i in range(10):
    print(i,end=' ')    #0 1 2 3 4 5 6 7 8 9
print(' ')

for i in range(0,10):
    print(i,end=' ')    #0 1 2 3 4 5 6 7 8 9
print(' ')

for i in range(5,10,2):
    print(i,end=' ')     #5 7 9

print(" ")

l=[1,2,4,7,8,78]
for i in range (1,len(l)-2):
    print(l[i],end=' ')  #2 4 7
print(" ")

# no argument no returntype
#  argument with returntype
# no argument with  returntype
#  argument no returntype