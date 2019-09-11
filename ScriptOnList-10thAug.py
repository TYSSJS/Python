l=[15,20,158,"hi",36.12,15,'kakun']
print(l)
print(l.count(15))  #2
print(l.index('kakun')) #6
l.remove(15)
print(l)    #[20, 158, 'hi', 36.12, 15, 'kakun']


l1=['g',152,"pattu"]
l.extend(l1)
print(l)     #[20, 158, 'hi', 36.12, 15, 'kakun', 'g', 152, 'pattu']

l.insert(2,"abhi")
print(l)
l.pop(5)    #[20, 158, 'abhi', 'hi', 36.12, 15, 'kakun', 'g', 152, 'pattu']
print(l)  #[20, 158, 'abhi', 'hi', 36.12, 'kakun', 'g', 152, 'pattu']


l2=[2,25,78,45,21,15,12]
l2.sort()
print(l2)   #[78, 45, 25, 21, 15, 12, 2]
l2.reverse()
print(l2)  #[78, 45, 25, 21, 15, 12, 2]
print(l2)  #[78, 45, 25, 21, 15, 12, 2]
l2copy=l2.copy()
print(l2copy) #[78, 45, 25, 21, 15, 12, 2]

l2.append("hello")
print(l2) #[78, 45, 25, 21, 15, 12, 2, 'hello']