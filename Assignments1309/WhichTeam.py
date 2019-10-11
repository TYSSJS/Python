JS_students = ['Praveen', 'Akshay', 'Amitab', 'Manish', 'Ritika']
PY_students = ['Abhishek', 'Afifa', 'Saloni', 'Anaconda', 'Prashant']
name = input("Enter name: ")
if name in JS_students:
    print("JS student")
elif name in PY_students:
    print("PY Student")
else:
    print("Student doesn't exist")
    

# case sensitive X
# flag = 0
# for s1 in JS_students:
#     flag += 1
#     if name.lower() == s1.lower():
#         print("JS student")
# for s2 in PY_students:
#     flag +=1
#     if name.lower() == s2.lower():
#         print("PY student")
# if flag == 10:
#     print("not a valid name")