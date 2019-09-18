a=int(input("enter a"))
b=int(input("enter b"))
try:
    res=a/b
    print(res)
# except ZeroDivisionError as z:
#     print(z)
#     print("caught and handled")
except Exception:
    print("this is supermost exception class")
finally:
    print("eno of the program")

