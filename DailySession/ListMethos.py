l=[1,2,3,4,5,6,7]
print(l[3:])
print(l[:])
print("reverse=",l[::-1])
# slicing operator
print(l[:])
# print("last value to be excluded")
print("Values",l[3::-1])

# WAP to print zero to 9 inside a list
# List comprehension
for i in range(10):
    l.append(i)
print(l)
print(" ")
# above program in one line as written below
# List comprehension
print([i for i in range(10)])    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# type cast the list to set and tuple for list comprehension
print(set([i for i in range(10)]))
print(tuple([i for i in range(10)]))