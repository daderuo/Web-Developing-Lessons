from  Shop import  Shop
import sys


PotatoShop = Shop(5,1.2)


while True:
    number = int(input("How many items do you want to buy? "))
    if PotatoShop.itemBuy(number) == True:
        print("Next customer")
    else:
        print("Bye Bye")
        sys.exit(1)
