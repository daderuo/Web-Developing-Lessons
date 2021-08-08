class Shop():
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        self.Total = 0

    def itemBuy(self, number):
        if self.quantity == 0:
            return 0
        elif self.quantity-number < 0:
            print(f"Not possible to buy {number} items, we have only {self.quantity}")
            return 1
        else:
            gain = self.price * number
            self.Total += gain
            self.quantity -= number
            print(f"The bill is: {gain}")
            return 1  