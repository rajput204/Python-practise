class MinimumBalanceerror(Exception): #it will inherit from the exceptional class overrirding
    def __init__(self,message):
      self.message=message
    def __str__(self):
       return self.message
class Account:
    count=100
    def __init__(self,account,balance):
        self.account=account
        self.balance=balance
        self.id='e'+str(Account.count+1)
        Account.count+=1
    def withdraw(self,amount):
            if self.balance<1000:
             raise MinimumBalanceerror("insufficient balance") #user defined exception
            self.balance=self.balance-amount
    def showbalance(self):
       return self.balance
    def deposit(self,amount):
       self.balance=self.balance+amount 
    def showdetails(self):
        print("account:-",self.account)  
        print("balance:-",self.balance)
        print("id:-",self.id)
    @classmethod
    def account(cls):
        return cls.count
a=Account("sbi",1000)
a1=Account("indian",1001)
print(a.showbalance())
a.withdraw(500)
print(a.showbalance())
print(chr(4)*10)
a.showdetails()
print(Account.account())
print(chr(4)*10)
a1.showdetails()
        