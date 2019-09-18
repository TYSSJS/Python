f=open('file1.txt','w')
# if file is not created , the above line will automatically create it
data='Good Afternoon'
f.write(data)
print("successfully written in file1.txt")
# print in console shows the above code executed successfully

f=open('file1.txt','r')
data=f.read()
print("read data",data)

f=open('file1.txt','r')
data=f.readline()
print("read data",data)