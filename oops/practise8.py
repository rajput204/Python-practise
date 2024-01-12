class account:
    account_no=1001
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.account='e'+str(account.account_no)
        account.account_no+=1
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount<1000:
            raise MinimumbalanceError('bank is empty')
        self.balance-=amount
    @classmethod
    def account(cls):
        return cls.account_no
    def showdetails(self):
        print(self.name)
        print(self.balance)
        print(self.account)
    def showbalance(self):
        return self.balance
a=account('aditya',2000,)
print(chr(4)*25)
a.showdetails()
print(account.account())
a.withdraw(500)
print(a.showbalance())
print(chr(4)*25)
a.deposit(50000)
print(a.showbalance())

