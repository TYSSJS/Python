d={'a':"TYSS",'b':"IBM",'c':"GOOGLE"}
print(d.keys())  #dict_keys(['a', 'b', 'c'])
print(d.values())   #dict_values(['TYSS', 'IBM', 'GOOGLE'])

d1=d.copy()
print(d1)  #{'a': 'TYSS', 'b': 'IBM', 'c': 'GOOGLE'}

d1.clear()
print(d1)    #{}
d.setdefault('d',"IBS")     #{'a': 'TYSS', 'b': 'IBM', 'c': 'GOOGLE', 'd': 'IBS'}
print(d)
d.pop('a')
print(d)   #{'b': 'IBM', 'c': 'GOOGLE', 'd': 'IBS'}

print(d.get('d'))  #IBS
print(d.get('IBS'))
print(d.values())
