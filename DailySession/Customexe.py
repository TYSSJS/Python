# customized exception - excception created by the user
# It can be used in other class.
class AgeInvalidError(Exception):
    def ageError(self):
        print("Age Invalid")

    age=int(input("Enter age"))
    if age>18:
        print("issue DL")
    else:
        raise ageError
    # except Exception:
         # print("super class exception ")

