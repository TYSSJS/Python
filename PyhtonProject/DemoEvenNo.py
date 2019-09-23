l = [1,2,3,4,5,6,7,8,9,12,57,88]
print([l[i]%2 == 0 for i in range(0,len(l))])

even = lambda l:l%2==0
print(even(l[2])) #returns boolean

even = list(filter (lambda l:l%2 == 0, l))
print(even)