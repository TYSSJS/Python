class Employee():
    def __init__(self,EmpID,EmpName,EmpPhoneNo,EmpSalary,EmpAddress):
        self.Id=EmpID
        self.Name=EmpName
        self.PhoneNo=EmpPhoneNo
        self.Salary=EmpSalary
        self.Address=EmpAddress
    def getEmployeeDetails(self):
        l=[self.Name, self.PhoneNo, self.Salary,self.Address]
        d.setdefault(self.Id,l)

print("--EMPLOYEE DETAILS--")
d={}
no_of_users=int(input("Enter the number of users"))
for i in range(0,no_of_users):
    EmpId=input("Enter the Employee id")
    EmpName=input("Enter the Employee name")
    EmpPhoneNo=input("Enter the Employee phone number")
    EmpSalary=input("Enter the Employee Salary")
    EmpAddress=input("Enter the Employee address")
obj=Employee(EmpId,EmpName,EmpPhoneNo,EmpSalary,EmpAddress)
obj.getEmployeeDetails()
keyinput=input("Enter the key")
d.get(keyinput)
print(d)
