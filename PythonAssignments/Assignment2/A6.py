class bank():
    def __init__(self,name,accno,ifsc,branch):
        self.name=name
        self.accno=accno
        self.ifsc=ifsc
        self.branch=branch
        l=[name,ifsc,branch]
        d.setdefault(accno,l)

d={}
n=int(input("enter number of employee"))
for i in range(n):
    name=input("enter name")
    accno=input("enter account number")
    ifsc=int(input("enter ifsc code"))
    ph=int(input("enter phone number"))
    branch=input("enter branch name")
    o1=bank(name,accno,ifsc,branch)

#key=list(d.keys())
key=input("enter accno to search")
print(d.get(key))

