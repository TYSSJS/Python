import json
f = open("jsonfile.txt","w")
data = {"q1":"btr","q2":"rajajinagar","q3":"banaswadi"}
jsdata = json.dumps(data)
f.write(jsdata)
print("done")