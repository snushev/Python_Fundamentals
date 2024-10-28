class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f"Current Balance: {self.balance}"


account1 = BankAccount("Gosho")
account1.deposit(1000)
print(account1.get_balance())

account1.withdraw(400)
