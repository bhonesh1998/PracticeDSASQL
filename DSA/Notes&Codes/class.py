class item:

    def __init__(self):
        print("I am created ! ")  # this method will be called automatically when we create instance of a class

    def calculate_total_price(self,p1,p2):
        return p1*p2


item1 = item()

item1.name = "Iphone"
item1.price = 10
item1.quantity = 2
total_cost = item1.calculate_total_price(item1.price,item1.quantity)

print(total_cost)





