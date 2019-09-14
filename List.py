l=[1,5.28,"hi",58,10,1]
print(l.count(1))
print(l)
# reverse by method and by slicing

l.reverse()
print("using inbuilt method", l)
print("using slicing-", l[::-1])   # [68.26, 'hg', 58, 15, 1, 5.28, 'hi', 58, 10, 1]
#   l[st:end:update]
#   if we are not giving any value it will take default values and print from -1 index


# reverse the list element upto a particular index
print(l[3::-1])  # ['hi', 58, 10, 1]
print(l[5::-1])  # [1, 5.28, 'hi', 58, 10, 1]


l1=[15,58,"hg",68.26]
l.extend(l1)
print("copied the list given" ,l)
print("last element", l[-1])

# slicing

print("print elements from particular indexes- ", l[0:3]) #[1, 10, 58]
print("skip elements from given idex " ,l[0:8:3])       # [1, 'hi', 15]

print("from start to last-" ,l[0:len(l)])               # print(l[0:len(l)])
print("from start to last-", l[:])                      # [1, 10, 58, 'hi', 5.28, 1, 15, 58, 'hg', 68.26]
print("from a particular index to last -",l[4:])        # [5.28, 1, 15, 58, 'hg', 68.26]



# print the numbers from 0 to 9 in a list

list=[]
for i in range(0,10):
    list.append(i)
print(list)             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# or
list.append(range(10))
print(list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, range(0, 10)]

# List comprehenssion
print([i for i in range(10)])        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# typecast to set and tuple
print(set([i for i in range(10)]))   # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(tuple([i for i in range(10)]))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9

