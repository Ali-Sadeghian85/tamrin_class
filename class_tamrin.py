class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    balance=0
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("you have not money enough")
        return self.balance
    def __str__(self):
        r=f"owner:{self.owner},balance:{self.balance}"
        return r
class SavingAcconunt(BankAccount):
    def __init__(self, owner, balance):
        BankAccount.__init__(self,owner,balance)
    def add_interest(self,rate):
        rate=(rate+100)/100
        self.balance=self.balance*rate
        return self.balance
acc1=BankAccount("Ali",1000)
acc1=acc1.deposit(1500)
print(acc1)
acc2=SavingAcconunt("Sara",2000)
acc2=acc2.add_interest(10)
print(acc2)



