s='good afternoon'
print(s.replace("o",'$'))
print(s.replace("good","bad"))
print(s.__add__('zzz'))
print(s.capitalize())
print(s.count('o'))
print(s.isnumeric())
print(s.__contains__('o'))
print(s.isspace())
print(' bye '.join(s))
print(s.index('o'))
print(s.startswith('g'))
print(s.isalnum())
print(s.isalpha())
print(s.title())
print(s.upper())
print(s.split(" "))
print(s.islower())
print(s.isupper())


# List Methods


l = [1, 2, 3.0, 4, 4, 'hi']
print(l.count(4))
print(l.index('hi'))
l.reverse()
print(l)
l.remove(4)
print(l)
l1=['hello', 'bye']
l.extend(l1)
print(l)
l.insert(2, 'morning')
print(l)
l.pop(3)
print(l)
l.append("good")
print(l)
b=l.copy()
print(b)
b.clear()
print(b)
c=[12,87,20,12,8]
c.sort()
print(c)
print(c.__len__())