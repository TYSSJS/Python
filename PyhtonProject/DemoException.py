try:
    a = int(input("a"))
    b = int(input("b"))
    s = a / b
    print(s)

except ZeroDivisionError:
    print("uh ho")