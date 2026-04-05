class debit:  # parent class
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def trans(self,amount):
        self.balance-=amount

class credit: # parent class

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def trans(self,amount):
        self.balance+=amount

class bank(credit,debit): # child class
    def __init__(self,balance):
        self.balance=balance

sbi = bank(100)
sbi.trans(30)
print(sbi.balance)













