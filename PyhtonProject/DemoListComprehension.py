# lst = []
# l = []
# l1 = []
# n = int(input("enter number of element: "))
# print("print number. But should be  between 0 to 9 ")
# for i in range(0, n):
#     element = int(input())
#     lst.append(element)
#     l1.extend(l)
#
# print(lst)

l = []
for i in range(0,10):
    l.append(i)
print(l)

print([i for i in range(10)])  #list comprehension

print({i for i in range(10)})  # set comprehension

print(set([i for i in range(10)])) # set comprehension

print((i for i in range(10)))     # tupple comprehension

print(tuple([i for i in range(10)]))  # tupple comprehension

