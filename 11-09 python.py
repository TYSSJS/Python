s="python script language"
# only first letter upper
print(s.capitalize())
# Python script language

# only first letter of each word upper
print(s.title())
# Python Script Language
print('ab c'.isalpha())
# false
print('abc43'.isalnum())
# false
print('hello'.isspace())
# false
print('hello'.startswith('h'))
# true
print('hello'.endswith('o'))
# true
s1 = "world wide web"
print(s1.count('w', 4))
# 2
print(s1.count('w', 4, 8))
# 1
print(s1.index('w'))
# 0
print(s1.index('w', 6, 10))
# 6
print(s1.find('web'))
# 11
s2='hi bye'
print(s2.replace('hi','hello'))
# hello bye
print(s2)
# hi bye
print(s2.__add__(' good'))
# hi bye good
print(s1.split('w'))
# ['', 'orld ', 'ide ', 'eb']
print(s1.split('w', 1))
# ['', 'orld wide web']
print(s1.split('w', 2))
# ['', 'orld ', 'ide web']
print('hello'.join('xyz'))
z = s1.split()
print(" abc ".join(z))
l=[12,45,87,'hi',87]
print(l.count(87))
print(l.index('hi'))
print(l.remove(87))
print(l)
l2=[98,1.2,'salu']
l.extend(l2)
print(l)
l.insert(2, 'bye')
print(l)
l.pop(2)
print(l)
l.reverse()
print(l)
a=l.copy()
print(a)
l.append('we')
print(l)
