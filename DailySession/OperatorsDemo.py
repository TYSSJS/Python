print(2+1)
print(2-1)
print(2*1)
print(5/10)
print("floor division=",5//10)
# only display the integer value in the decimal number
print("floor division",45//2)
print("5 power of 2",5**2)
print("exponential 10 powerof2",5e2)
# Assignment operator
a=4
a1=4
b=2
print(a1==b & a1==a)
# print(a==a1|a=b)
# Logical operator
a=1
a+=1
print(a)
b=1
b-=2
print(b)
# Relational operator
# Bitwise
# Membership operator
ls=[1,2,3,4,5,1,2,3]
print(1 in ls)
print(78 in ls)
print(5 not in ls)
# 5 is present in ls
print(55 not in ls)
"""55 is not present in the list, hence true"""
# Identity operator
a1=[1,2,3,4]
print(id(a1))
b1=a1;
b1=[1,2,3,4,5]
print(b1)
print(id(b1))
print(a1)
# here both the values will be different, since we are creating a new variable and trying to add the value
# but use append on the same varible will give same address
print(b1 is a1 )
print(b1 is not a)
# 'is' and 'is not' are the identity operators
# in identy opeartor they will check the address
# in membership python will check the value whereas in identity it will check tha address
