# l=[2,1,3,4,5,6,7,7,6]
# for i in l:
#     if i%2==0:
#         print(i,end=" ")

# l=[2,1,3,4,5,6,7,7,6]
# even=lambda l:l%2==0
# print(even(l[3]))

li=[2,1,3,4,5,6,7,7,6]
a=list(filter(lambda l:l%2==0,li))
print(a)

