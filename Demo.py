s1="hello"
print(s1.upper())
print("HI".lower())
print(s1.islower())
print(s1.isupper())

s2="python is scripting language"
print(s2.capitalize())
print(s2.title())

s3="hi"
print(s3.isalpha())
print('anu12#'.isalnum())
print('anu12'.isalnum())

print(' '.isspace())
# only space will be taken by isspace()
print('hi hello'.isspace())
print(' hi'.isspace())

print('hi'.startswith('h'))
print('hello'.endswith('o'))
print(s1.count('l'))
print(s1.count('a'))
# count of 'a' is not present in s1

s4="hi hello world"
print(s4.count('h'))
print(s4.count('h',3))

s5="world wide web"
print(s5.count('w',3))
# this will give the count of w
print(s5.count('w',6,10))
print(s5.index('w'))
# first matching index
print(s5.index('w',6))
print("check index")
print(s5.index('w',1,13))
print(s5.find('web'))

s='hi good morning'
print(s.replace('morning','evening'))

print(s4.split())
print(s4.split('w'))
print(s4.split('h'))
# split from the space
# in python we say 'none'
print(s5.split('d'))
print(s5.split('w'))
print(s5.split('w',2))
# split the first occurrences of 'w'

s6="this is a python class"
q=s6.split()
print(q)
z="@".join(q)
print(z)
# will split the string and than join the '@' with the split string
