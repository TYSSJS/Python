class BankDetails():
    def __init__(self, name, accNo, balance, bankName):
        self.name = name
        self.accNo = accNo
        self.balance = balance
        self.bankName = bankName

    def customerDetails(self):
        l=[name,balance, bankName]
        d.setdefault(accNo,l)

d={}
no_of_users = int(input("enter how many customers details u want to add"))
for i in range(0,no_of_users):
    name = input("enter the customer name")
    accNo = input("enter account number of customer")
    balance = input("enter balance of customer")
    bankName = input("enter the bank name of customer")
    obj = BankDetails(name, accNo, balance, bankName)
    obj.customerDetails()
print(d)
key = input("enter the account Number whose details u want to see")
print(d.get(key))
