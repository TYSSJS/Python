s = input("enter the string")
ch =[]
dl = []
scl = []
for i in range(0,len(s)):
    if s[i].isalpha():
        ch.append(s[i])
    elif s[i].isdigit():
       dl.append(s[i])
    else:
        scl.append(s[i])
print("     characters in string ",ch)
print("     special characters in string",scl)
print("     digits in string",dl)