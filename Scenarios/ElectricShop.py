from Classes.Costumer import Costumer
from Classes.Product import Product
from Classes.Store import Store
import random

keyboard = Product("Keyboard", "MQ653",143,"Computer Accessories")
monitor = Product("Monitor", "HP1567",250,"Screens")
oven = Product("Oven", "AFQ1347",100,"Kitchen")
refrigerator = Product("Refrigerator", "WQRQQ185",75,"Kitchen")
tv = Product("TV", "1234ASC",500,"Screens")

electric_shop = Store("zazi bazazi")
electric_shop.store_inventory.add_product(keyboard, 10)
electric_shop.store_inventory.add_product(monitor, 5)
electric_shop.store_inventory.add_product(oven, 2)
electric_shop.store_inventory.add_product(refrigerator, 8)
electric_shop.store_inventory.add_product(tv, 20)

costumer = Costumer("Yagor", 32)
electric_shop.costumers.append(costumer)

costumer.cart.add_product(keyboard, 3)

electric_shop.costumer_payment(costumer)

print(electric_shop.store_inventory)
