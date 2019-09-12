s={1,2,34,56,2,1}
print(s)  #{56, 1, 2, 34}
s.add(58)
print(s)  #{1, 2, 34, 56, 58}
s1=s.copy()
print(s1) #{1, 2, 34, 56, 58}
print(id(s))   #2764536042216
print(id(s1))  #2764567187528

##difference it creates

s.remove(1)
print(s)    #{2, 34, 56, 58}
s.pop()
print(s)  #{34, 56, 58}
s.pop()
print(s)  #{56, 58}

s.update(s1)
print(s)  #{1, 2, 34, 56, 58}

x={1,2,3,54}
y={1,2}
print(x.difference(y))  #{3, 54}

x.discard(3)
print(x)    #{1, 2, 54}

print(x.intersection(y))  #{1, 2}

print(id(x))  #address-3086319850888

print(x.issuperset(y))  #true
print(y.issubset(x))   #True




