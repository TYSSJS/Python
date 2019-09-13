#WAP to print numbers which are divisible from 5,10 and 15 range(200 to 999)
for i in range(200,999):
    if i%15==0 and i%10==0:
        print(i)
    else:
        continue