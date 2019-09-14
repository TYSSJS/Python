l=[1,2,3,'hi','6']
l.reverse()
print(l)
#or
l[::-1]
print(l)
#or
l[0:len(l)] #print an entire list rom 0 to last
print(l)
#or
print(l[0:])  #without end index also it will print entire list

#or
print(l[:])  #same as above

#reversing a string
s='adfg'
for i in s[::-1]:
    print(i,end=' ')

l1=[1,2,3,'hi',2,1,'bye']
print("start to last",l1[:])
#print("last ro first",l1[::-1])
print(l1[::-2])
print(l1[::-3])
print(l1[-4:-1])
print(l1[1:-1:2])
print(l1[1:-2:2])
print(l1[1:-2:3])
#reverse from 2 to 1 i.e; last but one to first element
#print(l1[3::-1])

#wap to print the values from 0-9 inside a list
l=[]
for i in range(0,9):
    l.append(i)
    print(l)
#List comprehension
print([i for i in range(10)])  #optimizing the code

#List comprehension type caste to set
print(set([i for i in range(10)]))
