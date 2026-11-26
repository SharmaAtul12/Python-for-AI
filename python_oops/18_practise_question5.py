# Use Dunder Function __gt__() to convey that order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
        


order1 = Order("Cold Drink", 50)
order2 = Order("Chips", 20)

res = order1 > order2
print(res) # This will print True because price of order1 is greater than price of order
