# a=int(input("Enter A-"))
# b=int(input("Enter B-"))
#
# try:
#     c = a / b
#     print("division-", c)
# except ZeroDivisionError:
#     print("denominator should not be 0")


# l = [10,25,58]
# i=int(input("enter the index-"))
# try:
#     print(l[i])
# except IndexError:
#     print("give proper index")
# except Exception:
#     print("from super class exception")
# finally:
#     print("operation is successful")


# class AgeInvalidError(Exception):
#     pass
#
#
# age=int(input("enter age"))
#
# if age>18:
#     print("issue DL")
# else:
#     raise AgeInvalidError("enter proper age")



class LoveFailureError(Exception):
    pass


nameBf = input("enter bf name=")
nameGF = input("enter gf name=")

if nameBf[0] == "Z" and nameGF[0] == "Q":
    print("successful couple")
else:
    raise LoveFailureError

#
# class AgeInvalidError(Exception):
#     pass
#
#
# age = int(input("enter age"))
# try:
#     if age > 18:
#         print("issue DL")
#     else:
#         raise AgeInvalidError
#
# except:
#     print("enter proper age")
#
#
