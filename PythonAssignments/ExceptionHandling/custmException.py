# class AgeInvalidError(Exception):
#     pass
# age=int(input("enter age"))
# if age>18:
#     print("isssue DL")
# else:
#     raise AgeInvalidError

# class AgeInvalidError(Exception):
#     def ageError(self):
#         print("age invalid")
#
# age=int(input("enter age"))
# if age>18:
#     print("isssue DL")
# else:
#     raise AgeInvalidError("ageINVALID")

class AgeInvalidError(Exception):
    def ageError(self):
        print("age invalid")

age=int(input("enter age"))
try:
    if age>18:
        print("isssue DL")
    else:
        raise AgeInvalidError("ageINVALID")
except AgeInvalidError as a:
    print(a)