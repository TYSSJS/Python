l = [10, 12.34, 'hi',10]

# to count how many times an element is present
print(l.count(10))

# to display the index of first occurance of character
print(l.index('hi'))
# print(l.clear())

# to remove element from list: if we use remove() then it will reomve the first occurance of character
l.remove(10)
print(l)

# to extend the list
l1 = [1, 2, 3, 4, 'go']
l.extend(l1)
print(l)

l1.pop(1)
print("use of pop")
print(l1)

# to insert new value at specific index
l1.insert(2, "hello")
print(l1)

# to create copy of the list
l3 = l1.copy()
print(l3)

l4 = [1, 5, 2, 10, 6]
l4.sort()
print("after sorting")
print(l4)

l4.append('hi')
print(l4)