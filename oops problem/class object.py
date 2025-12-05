class BankAccount:
    def __init__(self):
        self.balance = int(input ("Enter the balance"))
        self.amount=int(input("Enter the amount"))

    def withdraw(self):

        self.balance -= self.amount

        print("after withdraw balance is :",self.balance)

    def deposit(self):
        self.balance += self.amount
        print("after deposite balance is :",self.balance)

b=BankAccount()
b.withdraw()
b.deposit()


