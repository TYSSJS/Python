dict={}
def details():
    time = int(input("how many employee details u want to add"))
    for i in range(0, time):
        empname = input("enter employee name")
        id = input("enter id number")
        phone_no = input("enter phone number")
        salary = input("enter salary")
        listt = [id,phone_no,salary]
        dict.setdefault(empname,listt)

    print(dict)
details()