a=int(input("enter a"))
b=int(input("enter b"))

if a==b:
    print(a, " & ", b, " are same ")
# elif a>=b:
#     print(a, " is greator than and equals to ",b)
#
# elif a<=b:
#     print("a is less than and equal to b.")
elif a>b:
    print(a, " is greator than ",b)
elif a<b:
    print(a, " is less than ",b)
else:
    print(a, " & ",b, " are not same ")
    a!=b