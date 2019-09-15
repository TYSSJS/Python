d = {"k1": "V1", "k2": "V2", "k3": "V3"}
k = input("Enter key you want to check")
for i in d.keys():
    if i == k:
        print("key is present")
        break
    else:
        print("key is not present")
        break
