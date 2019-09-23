# a = 1
# b = 2
#
# sum = lambda a,b : a + b
# print(sum(a,b))
#
# sub = lambda a,b : a - b
# print(sub(a,b))
#
# mul = lambda a,b : a * b
# print(mul(a,b))
#
# div = lambda a,b : a / b
# print(div(a,b))

# x = lambda a: a+10
# print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

