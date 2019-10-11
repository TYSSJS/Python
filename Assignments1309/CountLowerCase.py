s = "Hello How ARe You"
c = 0
for i in range(len(s)):
    if s[i].islower():
        c += 1
print("no of lower case character = ", c)
