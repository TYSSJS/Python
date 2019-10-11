
class BankAccount:

    def __init__(self, name, amount):
        self.name = name
        self.amount = int(amount)

    def credit(self, credit_amount):
        self.amount += int(credit_amount)

    def debit(self, debit_amount):
        self.amount -= int(debit_amount)

    def display_bank_details(self):
        print(f"Name : {self.name}")
        print(f"Account Balance : {self.amount}")


ac1 = BankAccount('person1', 5000)
ac1.display_bank_details()
ac1.credit(1000)
ac1.display_bank_details()
ac1.debit(3000)
ac1.display_bank_details()
