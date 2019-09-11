string = "Good afternoon"

# to replcae all o's with $
s2 = string.replace('o', '$')
print(s2)

# to replace "good" with "bad"
s3 = string.replace("good", "bad")
print(s3)

s1 = "Go green happy living"
# use all  string methods
s2 = s1.replace('o', 'l')
print(s2)
print(s1.index('g'))
print(s1.count('i'))
print(s1.isalnum())
print(s1.isalpha())
s4 = "hello world"
print(s4.capitalize())
print(s1.title())
print(s1.upper())
print(s1.lower())
print(s1.rfind('i'))
print(s1.startswith('G'))
print(s1.endswith('g'))
s5 = ' '
print(s5.isspace())
s2 = s1.split()
print(s2)
print("#".join(s2))
print(s2)
print(s1.isupper())
print(s1.islower())

#list use all methods
l1 = [1,2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
print(l1.count(1))
print(l1.index(3))
print(l1.sort())
print(l1.append('hi'))
print(l1)
l3 = l1.copy()
print(l3)
l1.pop(2)
print(l1)
l1.insert(6,2)
print(l1)
l1.remove(8)
print(l1)
l3 = ['hi', 'lo', 'bye']
l1.extend(l3)
print(l1)
l3.reverse()
print(l3)
l3.clear()
print(l3)