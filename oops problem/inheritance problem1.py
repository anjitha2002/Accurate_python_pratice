class Bankaccount:
    def __init__(self):
        self.balance =int(input ("Enter Balance"))
    def deposite(self):
        self.dep_amount=int(input("Enter the amount to deposite"))
        self.balance +=self.dep_amount
        print("balance after deposite :",self.balance)
        return self.balance
    def withdraw(self):
        self.with_amount=int(input("Enter the amount to withdraw"))
        self.balance -=self.with_amount

        return self.balance


class Minimum_Balance_Account(Bankaccount):
    def __init__(self):
        Bankaccount.__init__(self)
        self.minimum_balance=int(input("Enter the min balance:"))
    def withdraw1(self):
        self.with_amount=int(input("Enter the amount to withdraw"))
        if self.balance - self.with_amount < self.minimum_balance:
            print("Sorry , the min balance should be maintained so withdrawing is not possible ")
        else:
            Bankaccount.withdraw(self)

m=Minimum_Balance_Account()
m.withdraw1()



