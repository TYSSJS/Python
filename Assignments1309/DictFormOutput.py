limit = int(input("Enter the number of key pair values you want"))
user_dict = {}
for i in range(limit):
    key, value = input("Enter Key: "), input("Enter Value: ")
    user_dict.setdefault(key, value)
print(user_dict)
