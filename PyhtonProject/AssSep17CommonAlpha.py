s = "hey i am surbhi"
s1= "hello i am in bangalore"

r = s.split()
r1 = s1.split()
# print(r)
# print(r1)
for i in range(len(r)):
    for j in range(len(r1)):
        if r[i] in r1:
            print(r[i])