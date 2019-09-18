# f=open("count.txt","w")
# data=" hello good morning good evening"
# f.write(data)

f=open("count.txt","r")
# print(f.read())
s1=f.read()
s2=s1

for i in range(len(s1)):
    count = 0
    flag=False
    for j in range(0,i):
        if s1[j]==s1[i]:
            flag=True
            break

    if flag==False:
        for j in range(i,len(s1)):
            if s1[i]==s1[j]:
                count+=1
        print(s1[i]," = ",count)
