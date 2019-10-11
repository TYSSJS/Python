s="good afternoon"
print(s.replace('o','$'))
print(s.replace('good','bad'))

#String and List operations

s1= 'hello'
print(s1.upper()) # to upper case
print('HeLLO'.lower()) # all characters to lower case
print(s.capitalize())  # capitalize
print(s.title()) # title
print(s.isalpha()) # isalpha
print(s.isalnum()) #alnum
print(s.isnumeric()) # isnumeric
print(s.isspace()) # isspace
print(s.startswith('g'))  # startswith
print(s.endswith('n')) #endswith
print(s.count('o')) # count
print(s.index('n'))  # index
print(s.find('d')) #find
print(s.replace('o','$')) # replace
print(s.split('o')) #split
print(s.split('o',1)) #split
print("&".join(s.split())) # join

#List

l=[1,3,4.5,'hi',True,46]
l.append("hi")             #append
print(l.count(3))          #count
print(l)
l.remove(4.5)              #remove
print(l)
l.pop(0)                   #pop
print(l)
print(len(l))              #len
print(l.index(True))       #index
l.insert(3,'hello')        #insert
print(l)

l1 = l.copy()              #copy
print(l1)
toBeCopied = ['new', 'list', 23, True]
l.extend(toBeCopied)       #extend
print(l)
l2 = [34,56.5,12,78,34]
l2.sort()                  #sort
print(l2)
l2.reverse()               #reverse
print(l2)
