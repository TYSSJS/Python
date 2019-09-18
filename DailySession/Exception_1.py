a=int(input("enter A"))
b=int(input("enter B"))
try:
    c=a/b
    print("the division of 2 numbers",c)
except ZeroDivisionError:
    print("denominator should not be zero.")
except Exception:
    print("from super class exception")
finally:
    print("It is finally block")


# if divide by zero below error will be thrown:-
# Traceback (most recent call last):
# File "C:/Users/Amritha/PycharmProjects/PythonProject/Exception_1.py", line 3, in <module>
#   c=a/b
# ZeroDivisionError: division by zero

'''try:
l=[1,2,3]
l[3]
except IndexError as I:
    print("Index out of bound") 
'''
# IndexError: list index out of range

'''print("hi)'''
# SyntaxError: EOL while scanning string literal
# double cots are missing and exception occurs
# can be handled by try,except block to run the program in flow.