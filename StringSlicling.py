s = "python for life"

sList = s.split()
print("*"*10)

for i in range(0, len(sList)):
    print(sList[i])

print("*"*10)

print(s[2:-5])

print("*"*10)

_2ndO = s.index('o')
_2ndF = s.index('f')
print(s[s.index('o', _2ndO+1):s.index('f', _2ndF+1)])

print("*"*10)

for i in range(1,11):
    print(i, end=" ")
    print()
    #print("\n")

print("*"*10)

str="Good afternoon"
print(str.replace('o', '$'))

print("*"*10)

print(str.replace('Good', 'Bad'))

print("*"*10)



