# List Functions

list=[1, 'a', 'abhi', 5.6, 'git86', 589]
numList=[1, 8, 6, 4, 9, 2, 5, 3]

list.append(numList)
print(list)

list.pop(0)
print(numList)
list.insert(-1, 10)

list.extend(numList)
print(list)

list.remove('abhi')
print(list)

print(list.copy())

list.reverse()
print(list)

print(list.clear())