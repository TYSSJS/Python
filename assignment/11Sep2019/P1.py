s = "python is scripting language"
# To Capitalize only first letter we use capitalize()
print(s.capitalize())

# To convert only first letter of all words into capital we use title()
print(s.title())

# to check alphabet or not
print(s.isalpha())

s1 = "abc#123"
print(s1.isalnum())

# isspace is used to check only space: it will check only for space
s2 = ' '
print(s2.isspace())

# starts with
print(s1.startswith('a'))

# ends with
print(s1.endswith('3'))

# count of characters in string
print(s.count('l'))

# count of characters in string from to end index
print(s1.count('l', 1, 5))

s3 = "World wide web"
print(s3.count('w', 6, 10))

# index() will return index of first matching element
print(s3.index('w'))

# index from start index to end index
print(s3.count('w'), 6, 10)
print(s3.index('w'), 6)

# find() will return the firts index postion inside string
print(s3.find('web'))

print(s3.replace("wide", "global"))
print(s3)
print(s3.split())
print(s3.split('w'))
print(s3.split('W'))
print(s3.split('d'))
print(s3.split('e'), 1)

