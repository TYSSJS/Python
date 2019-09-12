en1 = input("enter the first emp name")
id1 = int(input("enter the first emp id"))
phno1 = int(input("enter the first emp phone number"))
sal1 = int(input("enter the first emp salary"))
en2 = input("enter the second emp name")
id2 = int(input("enter the second emp id"))
phno2 = int(input("enter the second emp phone number"))
sal2 = int(input("enter the second emp salary"))
l1 = [en1,id1,phno1,sal1]
l2 = [en2,id2,phno2,sal2]
if int(len(l1)) == int(len(l2)):
    if int(l1[3]) > int(l2[3]):
        print( en1," salary is greater")
    else:
        print(en2," salary is greater")
else:
    print("not comparable")

