class AgeInvalidError(Exception):
    pass

age=int(input("Enter age"))
try:
    if age>=18:
        print("issue DL")
    else:
        raise AgeInvalidError
# except Exception:
#     print("super class exception")
except AgeInvalidError:
    print("invalid age")