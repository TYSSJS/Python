l='good afternoon'
l1=l
print(l)
s=l.split('o')
print(s)
print('$'.join(s))

print(l1.replace('good','bad'))

s1='hi Riya good morning'
print(s1)
print(s1.replace('hi','hello'))
print(s1.split())
s2=s1
print(''.join(s2))
print(s2.replace('hi','hello'))

print(s1.index('hi'))
print(s1.startswith(' '))
print(s1.endswith('g'))
print(s1.startswith('hi'))

print(s1.count('h'))
print(s1.isspace())
print(s1.isalnum())
print(s1.isalpha())
print(s1.islower())
print(s1.isupper())
print(s1.istitle())
print(s1)

print(s1.capitalize())
print(s1.title())
print(s1.find('hi'))

print(s1.find('i',2))
print(s1.casefold())

