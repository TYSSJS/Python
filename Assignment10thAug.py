for i in range(1, 11):
    print(i,end=" ")
print(" ")
#o/p--> 1 2 3 4 5 6 7 8 9 10


for i in range(5, 26):
    print(i,end=" ")
print(" ")
#o/p-->5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25


for n in range(1,26):
    if n % 5==0:
        print(n, end=" ")
print(" ")
#o/p-->5 10 15 20 25



for num in range(1,101):
    if num % 2==0:
        print(num, end=" ")
print(" ")
#Even numbers
#o/p-->2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100


for num in range(1,101):
    if num % 2!=0:
        print(num, end=" ")
print(" ")
#odd numbers
#o/p-->1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

x=25
y=0
for num in range(x,y-1,-5):print(num, end=" ")
#o/p-->25 20 15 10 5 0
