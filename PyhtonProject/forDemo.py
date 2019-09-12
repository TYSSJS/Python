for i in range(10):
    print(i)


l = [1,2,3,4]
for i in l:
    print(i)

l = [1,2,3,4]
for i in range(2, len(l)):  #starts from 2 and ends to whatever the length of list is
    print("l:",i)

l = [1,2,3,4]
for i in range(2, -1):
    print(i)

l = [1,2,3,4]
for i in l:
    print(i,end=" ")

print()

l = [1,2,3,4]
length = len(l) - 1
for i in range(1,length):
    print(l[i],end=" ")

