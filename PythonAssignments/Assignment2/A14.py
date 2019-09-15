ch=input("enter character string")
count=0
for i in range(len(ch)):
    if ch[i].isdigit():
        count+=1
print("number of digits in string =", count)