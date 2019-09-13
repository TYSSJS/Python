d={}
l=[]
def printDetails(id,name,des,addr):
    l=[name,des,addr]
    d.setdefault(id,l)
    print(d)

for i in range(0,5):
    id=int(input("enter id of emp"))
    name=input("enter name of emp")
    des=input("enter designation of emp")
    addr=input("enter address of emp")
    # l=[name,des,addr]
    #
    # d.setdefault(id,l)
    printDetails(id,name,des,addr)