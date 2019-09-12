for i in range(1,10):
    if(i%2!=0):
        continue
    print(i,end=" ")  #2 4 6 8

for i in range(1,10):
    if(i%2!=0):
        print(i,end=" ")  #1 3 5 7 9
        continue
