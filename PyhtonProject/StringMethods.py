from builtins import print

s1 = "hello i aM surbhi"
print(s1.title())
print(s1.casefold())
print(s1.isalpha())
print(s1.isalnum())
print(" ".isspace())
print(s1.isspace())
print(s1.count("l"))
print("world wide web".count("w", 6, 10))
print(len(s1))
print("world wide web".index("w"))
print("world wide web".index("w", 6))
print("world wide web".find("web"))
print("hi".replace("hi","hello"))

s2 = "good morning"
print(s2.replace("morning", "afternoon"))
print(s2.__add__(" everyone"))

s3 = "world wide web"
print(s3.split())
print(s3.split("w"))
print(s3.split("w",1))
print(s3.split("w",2))
print(s3)
print(s3.join(s2))