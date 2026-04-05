
# st1 define the class by class name
# st2 def init
# st3 attributes of class
# st4 methods of class
# st5 create object - real world object
# st6 accessing class attributes and methods

# variable -> attributes
#
# function -> methods

class wallet: # class <class-name>

    def __init__(self,owner,balance,color):
        self.owner = owner
        self.balance = balance
        self.color = color

    def add_money(self,balance):
        self.balance += balance

    def spend_money(self,balance):
        temp = self.balance - balance
        if temp<0:
            print("Insufficient balance to spend , please add some money ! ")
        else:
            self.balance-=balance

    def wallet_info(self):
        print(f"The owner of the wallet is {self.owner} , balance is {self.balance} and color is {self.color} ")



aman_purse = wallet("Aman",100,"black") # object creation - real thing

# accessing class attributes and methods


aman_purse.wallet_info()
aman_purse.add_money(1000)
aman_purse.wallet_info()
aman_purse.spend_money(500)
aman_purse.wallet_info()

ram_purse = wallet("Ram",200,"white")
ram_purse.wallet_info()
ram_purse.spend_money(400)
ram_purse.wallet_info()




