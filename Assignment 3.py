#1. Read two values dynamically from the user & print it in console.
a = input("Enter the value a ")
b = input("Enter the value b ")
print('The value of a is ',a,' & the value of b is ', b)

# print(' ')
# 2. Compare two values dynamically & print the greater.
val1 = input("Enter the value val1 ")
val2 = input("Enter the value val2 ")

if(val1 > val2):
    print(val1,' is greater than ', val2)
else:
    print(val2, 'is lesser than ', val1)

#3. Compare 3 values & print which one is greater.
num1 = input('Enter the value first number ')
num2 = input('Enter the value second number')
num3 = input('Enter the value of third number ')

if(num1 > num2 and num1 and num3):
    print(num1, ' is greater than ', num2,' and', num3)

elif(num2 > num1 and num2 > num3):
    print(num2, ' is greater than ', num1,' and', num3)
else:
    print(num3, ' is greater than ', num2,' and', num1)

#4. Read the inputs form the user in the range of 0 to 9 & the respected o/p should be in respect to words.

list = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN','EIGHT', 'NINE']

taking = input("Enter the number")

print(list[int(taking)])

#5. Read the username from the user and print each character seperatley.

user = input('Enter your name ')

for i in range (len(user)):
    print(user[i])

#6. Read the input from the user and if it is special charcter it should print seperately.
str = input('Enter alphanumeric string')

alpha = ''
num = ''
spec = ''

for i in range (len(str)):
    if(str[i].isdigit()):
        num = num + str[i]
    elif(str[i] >= 'A' and str[i] <= 'Z') or (str[i] >= 'a' and str[i] <= 'z'):
        alpha = alpha + str[i]
    else:
        spec = spec + str[i]
print('Alpabets are ', alpha)
print('Numbers are ', num)
print('Special charcters are ', spec)

#8. GOOGLE first char is G, second char is O etc
str8 = 'GOOGLE'
list8 = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh','Eigth', 'Ninth']
for i in range (len(str8)):
    print(list8[i],'char is ',str8[i])

#9. Collect 2 employee details from the user and compare their salary.

user1 = input('Enter the name of the emplyoee 1: ')
sal1 = input('Enter your salary : ')

user2 = input('Enter the name of the emplyoee 2: ')
sal2 = input('Enter your salary : ')

if sal1 > sal2 :
    print(user1, 'is getting more salary than', user2)
else:
    print(user2, 'is getting more salary than', user1)

#10. print the numbers which are divisible by 5 from 1 to 50
for i in range(5, 50):
    if(i%5==0):
        print(i, end = ' ')
#11. program which is divisible by 5,  10 , 15 from the range between 200 to 999. (hint use if loop)
for i in range(200, 999):
    if (i % 5 == 0) and (i % 10 == 0) and (i % 15 == 0):
        print(i, end=' ')

#12. program to swap two numbers without using temp variables
a12 = input('Enter the first number you want to swap : ')
b12 = input('Enter the second number you want to swap: ')
a12, b12 = b12, a12
print(a12,' ', b12)

#13. program to reverse a number using inout methods
a13 = input('Enter the number you want ot reverse & make sure it is atleast 2 digit')
print('Enter the number you want ot reverse & make sure it is atleast 2 digit :')
print(input()[::-1])

reverse = ''
num = input('Enter the numbe you want to reverse : ')
for i in range(len(num), 0, -1):
    reverse = reverse + num[i-1]
print(reverse)

#14. program to check weather given string is palindrome or not
str14 = input('Enter any string to check weather palindrome : ')

if str14 == str14[::-1]:
    print('The given string is PALINDROME')
else:
    print('The given string is NOT a palindrome')

#15. program to calculate simple interst (ptr/100)
pAmount = 10000
r = 0.05
t = 2
num = pAmount*r*t
print(num/100)

#16. program to merge two list and append the result in one more list.
la16 = [1,2,3,4]
lb16 = [5,6,7,8]
la16.extend(lb16)
lc17 = la16.copy()
print(lc17)

#17. program to to perform addition, subtraction, division, multuplication by taking two numbers.

n1, n2 = 10,5

def add():
    print('Addition of ',n1,'and',n2,'is', n1+n2)
def sub():
    print('subtraction of ',n1,'and',n2,'is',n1-n2)
def mul():
    print('Multiplication of ',n1,'and',n2,'is',n1*n2)
def div():
    print('Division of ',n1,'and',n2,'is',n1/n2)
add()
sub()
mul()
div()

#18. program to demonstrate to all the methods of dictionary, tuple, sets.

d = {'c1':'tyss', 'c2':'google', 'c3':'IBM'}
print(d.get('c1'))
print(d.values())
print(d.keys())
print(d.setdefault('c4', 'MicroFocus'))
d1 = d.copy()
d1.clear()
print('Cleared Dictionary is ',d1)

s = {1,2,34,56,1,87}
print(s)
s.add('a')
print(s)
s.pop()
s.remove(2)
print(s)

sc = s.copy()
print(sc)
sc.clear()
print('s: ',sc)
s1 = {1,2,3,99,200}
s.update(s1)
print('The updated set s : ',s)

t = (11,12,13,14)
print (t)
print(t.count(11))
print(t.index(13))

#19. program to count the number of vowels in the string
vowels=0
str = 'Mr. Professor'
for i in str:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print('Number of vowels are:', vowels)

#20.Swap first 2 and last 2 elements inside the list.
l1 = [10,20,30,40,50]

l1[0], l1[-1] = l1[-1], l1[0]
print(l1)
