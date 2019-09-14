print(5+4)
print(5-4)
print(5*4)
print(5/4)  #1.25
print(10%3) #1
print("floor division-"  ,20//8)  #2-round numbers
print(5**3) #125-power
print(2e2)  #200.0-exponetioal value
print(2*2**2) #8

# MEMBERSHIP OPTR  (in, not in)
a=[1,2,3,4,5,6,4,1,2,23]

print(a.index(1))  #0
print(1 in a) #True #–returns Boolean
print(23 not in a)  #False
print(100 not in a)  #True-


#Identity Optr  (is not,is)-points address
a=[1,2,3,4]
b=a;
print(id(a))  #2334450013960
print(id(b))  #32334450013960
print(b is a)  #True
print(b is not a) #False
a.append(20)
print(b)  #[1, 2, 3, 4, 20]  (only works for append())

b=[7,8,1,2] #(manually if we r creating  a list it creates diff object)
print(id(b))  #1905062579848
print(id(a))
print(b)  #[7, 8, 1, 2]
print(a)  #[1, 2, 3, 4]


