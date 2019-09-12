num = 145
res = 0
while(num>0):
    d = num%10
    num = int(num / 10)
    res = res * 10 + d

print(res)

