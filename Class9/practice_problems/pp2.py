#class methods
class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        return self.balance


my_account = BankAccount()
my_account.deposit(40)
my_account.withdraw(5)
my_account.deposit(10)




