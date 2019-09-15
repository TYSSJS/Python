d={}
l=[]
class bank():

    def __init__(self,name,accno,bal):
        self.name=name
        self.accno=accno
        self.bal=bal
        l=[self.name,self.bal]
        d.setdefault(self.accno,l)
    def modifybal(ac,bal):
        l[1]+=bal
        d.update(acc,l)
        print(print(d))
        # print(d)
n=int(input("enter number of customers"))
for i in range(n):
    name=input("name")
    accno=int(input("accno"))
    bal=float(input("balance"))
    b=bank(name,accno,bal)
print(d)

acc=int(input("enter account number to credit"))
amt=float(input("entere amount"))
for j in d:
    if acc==j:
        b.modifybal(j,amt)
        print(d.get(acc))
        break
print("end")
