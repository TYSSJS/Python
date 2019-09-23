#custom exception
class AgeInvalidError(Exception):
    pass
age = int(input("enter age"))
try:
    if age > 18:
        print("issue DL")
    else:
        raise AgeInvalidError("age invalid")
except Exception:
    print("super class exception")