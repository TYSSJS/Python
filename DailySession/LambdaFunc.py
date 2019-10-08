# FUNCTIONS OF LAMBDA
# REDUCE AND MAP
# sum each element in the system by itself
# l=[1,2,3]
# case1:
# for i in range(len(l)):
#     print(l[i]+l[i], end= " ")
# print(" ")
# case2:
# print([l[i]+l[i]for i in range(len(l))])

# case3:
# z=list(map(lambda x:x+x,l))
# print(z)

# Add two list
# list1=[1,2,3]
# list2=[2,3,4]
# l=list(map(lambda x,y:x+y,list1,list2))
# print(l)
# map will modify each and every function inside the list.
# map is a anonymous fuction
# map(function,
# import functools
# list=[1,2,3]
# print(functools.reduce(lambda a, b: a + b, list))
# reduce the complete list to one value
# add the internal elements to one value
# for this need to import functools