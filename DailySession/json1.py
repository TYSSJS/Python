
import json
# f=open("jsonfile.txt",'w')
# data={'q1':'btm','q2':'rajajinagar','q3':'oldairport'}
# jsdata=json.dumps(data)
# f.write(jsdata)
# print("success")

f=open("jsonfile.txt",'r')
data=f.read()
jsondata=json.loads(data)
print("json data",jsondata)
# C:\Users\Amritha\PycharmProjects\pySelenium\Sony100Questions.py