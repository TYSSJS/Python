num = int(input("enter the number to check"))
res = num

def fact(num):
    if num == 1:
        return 1
    else:
        return (num * fact(num-1))

while (num > 0):
    d = num % 10
    num = num / 10
    res = res + fact(d)

if res == num:
    print("number is strong number")
else:
    print("number is not strong number")