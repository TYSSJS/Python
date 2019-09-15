a = input("Enter year")
if int(a) % 4 == 0 or (int(a) % 4 == 0 and int(a) % 100 != 0):
    print("its a leap year")
else:
    print("not a leap year")