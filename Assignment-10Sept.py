#Assignments On  String (16 Methods)

s="good afternoon"
print(s.replace("o",'$'))  #g$$d aftern$$n
print(s.replace("good","bad"))  #bad afternoon

print(s.count("o"))  #4
print(s.index("g"))  #0
print(s.split(" "))  #['good', 'afternoon']
print(s.__add__(" 123"))
print(s.isnumeric())        #good afternoon 123
print(s.isalpha())           #False
print(s.isalnum())           #False
print(s.isspace())          #False
print(s.isalpha())          #False
print(s.startswith("g"))    #True
print(s.endswith("d"))      #False
print(s.capitalize())       #Good afternoon
print(s.title())            #Good Afternoon
print(s.islower())     #True
print(s.isupper())       #False
s1=s.split(" ")
print("*".join(s1))     #good*afternoon
print(s.__contains__("g"))  #True



#Assignments On List  (12 methods)

l=[20,'Annapurna',123,2.45,'b',20]
print(l)                    #[20, 'Annapurna', 123, 2.45, 'b', 20]
print(len(l))               #6
print(l.count(20))          #2
print(l.index(2.45))        #3

l.append("TYSS")
print(l)                    #[20, 'Annapurna', 123, 2.45, 'b', 20, 'TYSS']

l.insert(1,'python')
print(l)                    #[20, 'python', 'Annapurna', 123, 2.45, 'b', 20, 'TYSS']

l.remove('b')
print(l)                    #[20, 'python', 'Annapurna', 123, 2.45, 20, 'TYSS']

l.pop(3)
print(l)                     #[20, 'python', 'Annapurna', 2.45, 20, 'TYSS']

print(l.copy())             #[20, 'python', 'Annapurna', 2.45, 20, 'TYSS']

l.clear()
print(l)                #[]

l1=[20,14,58,12,10,36,124.0,1]
l1.reverse()
print(l1)                   #[1, 124.0, 36, 10, 12, 58, 14, 20]
l1.sort()
print(l1)                   #[1, 10, 12, 14, 20, 36, 58, 124.0]

l3=["abc,'xyz",'ab',125]
l3.extend(l1)
print(l3)                    #["abc,'xyz", 'ab', 125, 1, 10, 12, 14, 20, 36, 58, 124.0]