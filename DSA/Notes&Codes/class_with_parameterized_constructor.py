class item:

    def __init__(self, name:str, quantity:int ,price:float):
        self.name = name
        self.quantity=quantity
        self.price = price

    def calculate_total_price(self):
        return self.quantity * self.price



item1 = item("iphone",10,2)

cost = item1.calculate_total_price()

print(cost)



