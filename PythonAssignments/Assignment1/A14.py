#check whether the given string is palindrome or not
s=input("enter a string")
s1=""
# print("the original string is : ",s)
for i in range(len(s)-1,-1,-1):
    s1=s1+s[i]
if s==s1:
    print("palindrome")
else:
    print("not palindrome")