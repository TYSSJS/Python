#first letter p in upper case
s1="python for life"
print(s1.capitalize())

#all words first letter in uppercase
print(s1.title())
#op is true
print("afifa".isalpha())
#op is true
print("afif19".isalnum())
#op is true
print(' '.isspace())
#op is false
print('hello '.isspace())
#op is true
print('hello'.startswith('h'))
#op is false
print('hello'.startswith('e'))
#op is true
print('hello'.endswith('o'))
#op is 2
print('hello'.count('l'))
s2="world wide web"
#op is 2
print(s2.count('w',2))
#op is 2
print(s2.count('w',6,12))
#op is 1
print(s2.count('w',6,11))
#index of w is 0
print(s2.index('w'))
#index of w is 11
print(s2.index('w',11,13))
#starting index of word is returned
print(s2.find('web'))
s3='hi'
print(s3.replace('hi','bye'))
print(s3.__add__(' ' 'bye'))
print(s2.split('w'))
print(s2.split())

print(s2.split('w',1))
print(s2.split('w',2))
print(s2.split('d'))
print(s3.join("hello"))

#join
s="this is training"
z=s.split()
print(" hi ".join(z))
#List
l=[10,20.5,'bye',10]
print(l.count(10))
print(l.index('bye'))
l.remove(10)
print(l)
l1=[12,13.234,15664]
#adding one list to another
l.extend(l1)
print(l)
#insert element at a partuclar index value
l.insert(1,'hello')
print(l)
#to delete a particular element ,give index inside pop method
l.pop(5)
print(l)
#reverse the list
# l.reverse()
# print(l)
#copy
a=l.copy()
print(a)
#append
g=[1,3,2,6,5]
g.append((10))
print(g)
#sort
g.sort()
print(g)




