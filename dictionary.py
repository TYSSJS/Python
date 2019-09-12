d={'c1':'tyss','c2':'goolg','c3':'ibm'}
print(d.keys())
print(d.values())
print(d.setdefault('c3','ms'))
print(d.setdefault('c4','ms'))
print(d.items())
d1=d.copy()
print(d1)
print(d.get('c1'))

