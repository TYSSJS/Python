t=(11,12,13,14)
print(t)
# cannot change the value..not growable
# no modification not even replace
print(t.count(11))
print(t.index(13))

s={1,2,34,56,2,1}
# set values
print(s)
s.add('a')
print(s)
# will not be in same order
s.pop()
print(s)
s.remove(34)
pri

q=s.copy()
print(q)
q.clear()
print(q)
s1={1,2,3,99,200}
s.update(s1)
# few elements will update above the first, here no order
print(s)

# concatinate beteween two sets
# just string stmt in print to understand the print details
# print("s :",s)


