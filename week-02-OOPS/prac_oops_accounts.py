class Account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.acc=acc
    def credit(self,amount):
        self.balance+=amount
        print("rs.",amount,"is credited from your account.")
    def debit(self,amount):
        self.balance-=amount
        print("rs.",amount,"is debited to your account.")
    def bal(self):
        print(f"Your balance is {self.balance}")

acc1 = Account(1000,101)
print(acc1.balance)
acc1.bal()
acc1.debit(100)
acc1.bal()
acc1.credit(200)
acc1.bal()
        