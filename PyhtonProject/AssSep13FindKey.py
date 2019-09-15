d = {"1": "a", "2":"b", "3":"c"}
key = input("enter the key u want to search")
x = key in d
if x == True:
    print("key is there")
else:
    print("key is not there")