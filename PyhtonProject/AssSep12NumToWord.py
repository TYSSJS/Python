def listConvert():
    lst = []
    l = []
    l1=[]
    n = int(input("enter number of element: "))
    print("print number. But should be  between 0 to 9 ")
    for i in range(0,n):
        element = int(input())
        lst.append(element)

    print(lst)
    for i in range(0,n):
        c = convert(lst)
       # print(c)
        l.append(c)
    print(l)

def convert(lst):

    for i in range(0,len(lst)):

        if int(lst[i] == 0):
            print(lst)
            return "zero"

        elif lst[i] == 1:
            print(lst)
            return "one"

        elif lst[i] == 2:
            return "two"

        elif lst[i] == 3:
             return "three"

        elif lst[i] == 4:
            return "four"

        elif lst[i] == 5:
            return "five"

        elif lst[i] == 6:
            return "six"

        elif lst[i] == 7:
            return "seven"

        elif lst[i] == 8:
            return "eight"

        elif lst[i] == 9:
            return "nine"

        else:
            return "format not correct"
listConvert()