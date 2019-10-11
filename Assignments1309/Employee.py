class EmployeeDetails:
    id = 0

    def __init__(self, id, name, designation, blood_group):
        self.id = id
        self.name = name
        self.designation = designation
        self.blood_group = blood_group


Emp1 = EmployeeDetails(1, 'e1', 'Test Engineer', 'B+')
Emp2 = EmployeeDetails(2, 'e2', 'Tester', 'A+')
Emp3 = EmployeeDetails(3, 'e3', 'Dev', 'A+')
Emp4 = EmployeeDetails(4, 'e4', 'HR', 'O-')
Emp5 = EmployeeDetails(5, 'e5', 'Dev', 'AB+')
list_of_employees = [Emp1, Emp2, Emp3, Emp4, Emp5]
emp_id = int(input("Enter emp id: "))
for emp in list_of_employees:
    if emp_id == emp.id:
        print(f"Name : {emp.name}")
        print(f"Designation : {emp.designation}")
        print(f"Blood Group : {emp.blood_group}")
