import json
f=open("jsn1.txt","w")
data={'q1':'basavanagudi','q2':'BTM','q3':'old airport','q4':'rajajinagar'}
jsdata=json.dumps(data)
f.write(jsdata)
print("success")
