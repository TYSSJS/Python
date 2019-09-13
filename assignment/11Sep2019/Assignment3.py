# 1. WAP to print numbers divisible by 5 from 1 to 50
for i in range(1, 51):
    if i % 5 == 0:
        print(i,end=' ')
print(' ')

# 2. WAP to print numbers divisible by 5, 10, 15 from range 200 to 999
for i in range(200, 1000):
    if (i % 5 == 0) or (i % 10 == 0) or (i % 15 == 0):
        print(i,end =' ')
print(' ')

# 3. to swap 2 numbers
a = 10
b = 15
a,b = b,a
print(a)
print(b)

# 4. WAP to reverse a number
num = 1234
rev_num = 0
while(num != 0):
    rev_num = rev_num + rev_num % 10
    num = num/10
print(rev_num)


# 5.  WAP to check given string is palindrome or not
str = "maom"
rev = ''
len = len(str)
for i in range(0,len):
    rev = str[i]+rev
print(rev)
if str == rev:
    print("string is palindrome")
else:
    print("string is not palindrome")

# 6.  WAP to calculate simple interest
p = 12
t = 6
r = 2
simple_interest = (p*t*r)/100
print(simple_interest)

# 7. WAP to merge 2 lists & append the updated list in one more list
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['ji', 'ko', 'po', 3.2]
list1.extend(list2)
print(list1)
list3 = list1.copy()
print(list3)


# 8. WAP to perform calculator operation
a = 2
b = 3
print("addition of numbers ", a+b)
print("subtraction of numbers ", a-b)
print("multiplication of numbers ", a*b)
print("divison of numbers ", a/b)

# 9. WAP to demonstrate list, set, tuple, dictionary
l1 = [1, 2, 3, 4, 5, 'hi']
l1.append("bye")
print(l1)
l2 = l1.copy()
print(l2)
l1.reverse()
print(l1)
l1.insert(2,"lol")
print(l1)
l1.pop(3)
print(l1)
l1.remove(4)
print(l1)
print(l1.index(2))
print(l1.count(1))
l2 = ['lol', 'pop', 'ko', 2.2, 1, 7]
l1.extend(l2)
print(l1)
l1.reverse()
print(l1)
l1.clear()
l3 = [3, 45, 5, 60]
l3.sort()
print(l3)

# set methods
s = {1, 20, 3, 40, 5,'hi'}
s.add('bye')
print(s)
s1 = s.copy()
print(s1)
s2 = {70, 80, 90, 1, 2}
print(s.difference(s2))
s.remove(20)
print(s)
print("removed 20")
print(s.pop())

print(s.difference_update(s2))
s.discard(5)
print(s)
s3 = {80,90}
print(s2.issubset(s3))

# tuple methods
t = (1, 2, 3, 'hi', 6, 2.3, 'lol', 3)
print(t.count(3))
print(t.index(2))
print(t.__len__())

# dictionary methods
d1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
print(d1.values())
print(d1.keys())
d2 = d1.copy()
print(d2)
print(d1.get(2))
d2.pop(4)
print(d2)
d2.pop(5)
print(d2)
d2.items()
print(d2)
d2.popitem()
print(d2)
d2.clear()
print(d2)

# 11. Swap first 2 with last 2 elements inside the list



#10. Count the number of owels in the given string
str1 = "Gaoeoigolue"
le1 = str1.__len__()
print(le1)
str_owels = ''
vowel_count = 0
for i in range(0, le1):
    if str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u':
        vowel_count = vowel_count + 1
print(vowel_count)

