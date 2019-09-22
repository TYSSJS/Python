import json
f2=open("file1.txt","w")
data={"a1":"BTR","a2":"BTM","a3":"OAR"}
jsdata=json.dumps(data)
f2.write(jsdata)
print(f2.tell())


# read data in console

f=open("file1.txt","r")
# dat=f.read()
# jsondata=json.loads(dat)
# print("using loads method-",jsondata)


#load() is not taking string ,it takes the object
js=json.load(f)
print("using load method-", js)






