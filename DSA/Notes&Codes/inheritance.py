class item:

    def __init__(self, name:str, quantity:int ,price:float):
        self.name = name
        self.quantity=quantity
        self.price = price

    def calculate_total_price(self):
        return self.quantity * self.price


class phone(item):
    pass

    #
    # def calculate_total_price(self):
    #     return 10 * self.quantity * self.price



lava = phone("lava",1,200)
print(lava.calculate_total_price())




# item1 = item("iphone",10,2)
#
# cost = item1.calculate_total_price()
#
# print(cost)



