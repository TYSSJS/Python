# class Company():
#     def comName(self):
#         cname = input("enter the company name")
#         if(cname=='TYSS'):
#             print("Welcome to python")
# obj=Company()
# obj.comName()

class Empd():
    def emp_det(self,eid,ename,edept):
        self.eid=eid
        self.ename=ename
        self.edept=edept
d={
    'id1':['afifa','AT'],
    'id2':['saloni','MT'],
    'id3':['annu','dev']
   }
key=input("enter the key")
if key in d:
    print(d.get(key))

obj=Empd()
obj.emp_det('eid','ename','edept')
#
# class bank():
#     def details(self, acc, branch, name):
#         self.Account = acc
#         self.Branch = branch
#         self.Name = name
#         print("account- ", acc,"\n", "branch- ",branch,"\n", "name of branch- ",branch)
# obj=bank()
# obj.details(120831209, 'BTM', 'SBI')