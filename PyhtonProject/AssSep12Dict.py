key = input("enter key ")
value = input("enter value")
d = {}
d.setdefault(key,value)
print(d)
print(d.keys())
print(d.values())
d1 = d.copy()
print(d1)
d1.clear()
