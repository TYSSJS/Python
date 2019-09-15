l=[]
n=int(input("enter a number"))

def add(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    print(sum)

while n>0:
    e=int(input("enter an element"))
    l.append(e)
    n-=1
add(l)

