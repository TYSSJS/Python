# 1.Read 2 values dynamically from user & print them

a = input("enter a ")
b = input("enter b ")
print(a)
print(b)

# 2.Compare 2 values which one is greater
c = input("enter value c ")
d = input("enter value d ")
if a < b:
    print("a is smaller")
else:
    print("b is smaller")

# 3.Compare 3 values which one is greater
e = input("enter value e ")
if c > d and c > e:
    print("c is greater")
elif d > e and d > c :
    print("d is greater")
else:
    print("e is greater")

# 4. Covert number to word in the range 1 to 10
d1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
print(d1.values())


# 5. Read the username from the user & print each character seperately
username = input("enter username ")
strlen = len(username)
for i in range(strlen):
    print(username[i])

# 6. Read input from user & seperate all alphabets, characters,specialcharacter
s = input("enter string ")
slen = len(s)
alpha=''
digit = ''
specialchar = ''

for i in range(0, slen):
    if(s[i]>='a'and s[i]<='z'):
        alpha+=s[i]

    elif(s[i]>='0'and s[i]<='9'):
        digit+=s[i]

    else:
        specialchar+=s[i]

print(alpha,end= ' ')
print(digit,end=' ')
print(specialchar,end=' ')
print(' ')

# # 7. To print the employee details
def emp_details(name, eid, sal, phone):
    print("emp name is ", name)
    print("emp id is ", eid)
    print("emp sal is ", sal)
    print("emp phone is ", phone)


emp_details("John", 10, 45000, 97883426126531)
emp_details("honey", 12, 56789, 897655237821)



# 8. Given name "Google" print characters seperately
str1 = "Google"
str1_len = len(str1)
for i in range(str1_len):
    print(i+1,"st character is "+str1[i])

# Collect 2 employee details & compare their salaries
sal1 = 45000
sal2 = 34000


def emp_details(name, eid, sal1, phone):
    print("emp name is ", name)
    print("emp id is ", eid)
    print("emp sal is ", sal1)
    print("emp phone is ", phone)


def emp_details(name, eid, sal2, phone):
    print("emp name is ", name)
    print("emp id is ", eid)
    print("emp sal is ", sal2)
    print("emp phone is ", phone)


emp_details("John", 10, sal1, 97883426126531)
emp_details("honey", 12, sal2, 897655237821)

# comparing salaries
if sal1 < sal2:
    print("John salary is less than honey")
else:
    print("honey salary is less than John")
