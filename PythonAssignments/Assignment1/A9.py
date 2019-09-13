
name=input("name")
id=int(input("id"))
sal=int(input("salary"))
ph=int(input("ph.no"))
l1=[id,name,sal,ph]

name = input("name")
id = int(input("id"))
sal = int(input("salary"))
ph = int(input("ph.no"))
l2 = [id, name, sal, ph]

if l1[2]==l2[2]:
    print(l1[1]," is getting same salary as ",l2[1])
elif l1[2]>l2[2]:
    print(l1[1], " is getting more salary than ", l2[1])
else:
    print(l1[1], " is getting less salary than ", l2[1])