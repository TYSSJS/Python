import json
f = open("jsonfile.txt","r")
dat = f.read()
jsondata = json.loads(dat)
print("jspndata", jsondata)
