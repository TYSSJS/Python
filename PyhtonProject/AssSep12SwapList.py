def swap(l):
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    temp = l[1]
    l[1] = l[-2]
    l[-2] = temp
    return l

def listTo():
    l = []
    n = int(input("enter number of element : "))
    print("enter the numbers")
    for i in range(0,n):
        element = int(input())
        print("before swapping: ", l)
        l.append(element)
    l1 = swap(l)
    print("after swapping : ",l1)

listTo()