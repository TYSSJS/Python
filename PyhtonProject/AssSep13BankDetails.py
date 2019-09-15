class BankDetails():
    def __init__(self, name, accNo, balance, bankName):
        self.name = name
        self.accNo = accNo
        self.balance = balance
        self.bankName = bankName

    def display(self):
        print(self.name, self.accNo, self.balance, self.bankName)


no_of_users = int(input("enter how many customers details u want to add"))
for i in range(0,no_of_users):
    name = input("enter the customer name")
    accNo = input("enter account number of customer")
    balance = input("enter balance of customer")
    bankName = input("enter the bank name of customer")
    obj = BankDetails(name, accNo, balance, bankName)
    obj.display()
