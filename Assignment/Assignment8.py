#1.Write a program to multiply bot the list in a such a way that, it should print both the list combination one by one.
l1=[1,2,3,4]
l2=['a','b','c','d']
print([(i, j) for i in l1 for j in l2])

# l3=[(a,b) for a in l1 for b in l2 if a!=b]
# print(l3)

print(" ")

#2. Print the multiplication of 2
num=2
for i in range(1,11):
    print(num,'x',i,'=',num*i)
# print([(2,'x',i,'=', num * i) for i in range(1, 11)]) ->wrong


print(" ")

# 3. Print the tyss
count=3
str1='TYSS'
while(count):
    str=input("enter string:")
    if str==str1:
        print("It is in basvangudi")
        break
    else:
        print("invalid")
        count=count-1
        print(count)
print("success")







