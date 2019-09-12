# dictionary
d={'c1':'tyss','c2':'google','c3':'IBM'}
print(d.keys())
print(d.values())
d1=d.copy()
print(d1)
d.clear()
print(d)
d.setdefault('c3','google')
d.setdefault('c4',' ')
# always print one key and value
print(d)
print(d.get('c3'))

