class Shop():
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        self.Total = 0

    def itemBuy(self, number):
        if self.quantity-number < 0:
            print(f"Not possible to buy {number} items")
        else:
            gain = self.price * number
            self.Total += gain
            self.quantity -= number
            print(f"The bill is: {gain}")  