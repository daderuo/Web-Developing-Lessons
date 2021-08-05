from  Shop import  Shop


PotatoShop = Shop(5,1.2)


while True:
    number = int(input("How many items do you want to buy? "))
    PotatoShop.itemBuy(number)
    print("Bye Bye")