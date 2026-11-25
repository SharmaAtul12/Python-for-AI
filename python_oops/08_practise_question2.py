
class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def debit(self, money):
        if money > self.bal:
            print(f"Your Balance is {self.bal} , Please make your debit amount less .")
        else:
            self.bal = self.bal - money
            print(f"You Have Successfully Debited the amount :  {money} and remaining bal is {self.bal}")

    def credit(self, money):
        self.bal = self.bal + money
        print(f"You Have Successfully Credited the amount :  {money} and remaining bal is {self.bal}")

    def check_balance(self):
        print(f"Your Current Balance is : {self.bal}")

acc1 = Account(1000, 123456789)
acc1.check_balance()
acc1.debit(500)
acc1.credit(200)
acc1.check_balance()