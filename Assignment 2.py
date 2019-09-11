#'Good afternoon' ->replace all o with $; replce good with bad

s = 'good afternoon'
print(s.replace('o', '$'))

print(s.replace('good', 'bad'))

#take one string & apply all the methods

print('Title Method ', s.title())
print('Number of o in the string is ', s.count('o'))
print('Spliting the string ',s.split())
print('Using upper method',s.upper())
print('Using lower method',s.lower())
print('Using find method', s.find('a'))
print('Using index method', s.index('o'))
s4 = 'There is no shorcut for success'
print('Using index between first and last ',s4.index('s',5))

s1='@'.join(s)
print(s1)


print('Using count method', s4.count('s'))
print('Using starts with method ',s4.startswith('a'))
print('Using ends with method', s4.endswith('f'))

print('Using split method',s4.split())
print('Using isspace method', s.isspace())
print('Using isalnum mehtod',s.isalnum())
print('Using isalpha method',s.isalpha())
print('Using isdigit method', s.isdigit())

lis = [12,34,45,17,9,9]
print(lis.sort())
print(lis)
print(lis.remove(9))
print(lis)
print(lis.pop(3))
print(lis.reverse())
print(lis)

lis1 = lis.copy()
print('Printing the copy of the list',lis1)
lis2 = [15,78,36,'hi', 'bye']
print(lis1.extend(lis2))
print(lis1)










