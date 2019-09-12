word = input("enter a string")
res = ""
for i in range(len(word)-1,-1,-1):
    res = res + word[i]

if word == res:
    print("number is palindrome")
else:
    print("number is not palindrome")