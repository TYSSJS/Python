s="Good Morning"
a=s.replace('o','$')
print(a)

s2="Good Morning"
b=s2.replace('Good','Bad')
print(b)

s3="Hello everyone"
print(s3.replace('e','E'))
print(s3.index('o'))
print(s3.count('e'))
a=s3.split()

print('@ll'.join(a))
print(s3.find('llo'))
print(s3.startswith("H"))
print(s3.endswith("e"))
print(s3.isspace())
print(s3.isalnum())
print(s3.isalpha())
print(s3.title())
print(s3.capitalize())
print(s3.split('e'))
print(s3.islower())
print(s3.isupper())
print(s3.upper())
print(s3.lower())


l=[10,12,'Good',12.45, 12,12,'anvika']
print(l.count(10))
print(l.index(12.45))
print(l.remove(12))
cp=l.copy()
print(cp)
st=[10,3,9,1]
st.sort()
print(st)
print(l.reverse())
print(l.pop(1))
print(l.append('happy'))
print(l)
l2=[1,'kamy']
print(l.extend(l2))
print(l)
print(l.clear())
print(l)