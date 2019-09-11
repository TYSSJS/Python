s="hello good morning"
print(s.capitalize())
print(s.title())

s1='hi'
print(s1.isalpha())
print("asdf12".isalnum())
print('asd12@@'.isalnum())
print(' '.isspace()) #True
print(''.isspace()) #False
print(s.isspace()) #False
print(s.startswith('h'))
print(s.count('l')) #2

s1='hi hello world hello'
print(s1.count('h',1)) #2
print(s1.count(' '))
print(s1.count(' ',3))

s4="world wide  web"
print(s4.index('w'))
print(s1.count('w',6,10))
print(s4.index('w',6))
print(s4.index('e',6))

print(len(s4))
s5='good morning'
print(s5.replace('morning','evening'))
print(s5.__add__(' blore'))

print(s4.split(' '))
print(s4.split('w'))
print(s4.split('w',1))
print(s4.split('w',2))
print(s4.split('w',-1))