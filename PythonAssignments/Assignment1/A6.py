text=input("enter a string ")

cstr=""
astr=""
dstr=""
print(len(text))
for i in range(0,len(text)):
    if text[i].isdigit():
        dstr=dstr+text[i]
    elif text[i].isalpha():
        astr=astr+text[i]
    else:
        cstr=cstr+text[i]
print(astr)
print(dstr)
print(cstr)