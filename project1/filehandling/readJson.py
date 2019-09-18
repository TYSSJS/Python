import json
f=open("jsn1.txt","r")
d=f.read()
data=json.loads(d)
print("json data : ",data)