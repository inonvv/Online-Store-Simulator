from Classes.Costumer import Costumer
from Classes.Store import Store
from Data.Products import *

kley_zemer = Store("Kley Zemer")
kley_zemer.store_inventory.add_product(products_map["Guitar"], 5)
kley_zemer.store_inventory.add_product(products_map["Drums"], 3)
kley_zemer.store_inventory.add_product(products_map["Piano"], 2)
kley_zemer.store_inventory.add_product(products_map["Violin"], 7)
kley_zemer.store_inventory.add_product(products_map["Trumpet"], 10)

yanon = Costumer("yanon", 33)
lial = Costumer("lial", 35)
kley_zemer.costumers.append(yanon)
kley_zemer.costumers.append(lial)
yanon.cart.add_product(products_map["Guitar"], 2)
yanon.cart.add_product(products_map["Trumpet"], 5)
# make purchase
lial.cart.add_product(products_map["Violin"], 1)
lial.cart.add_product(products_map["Trumpet"], 7)

kley_zemer.costumer_payment(yanon)
kley_zemer.costumer_payment(lial)

print(kley_zemer.store_inventory)
print(kley_zemer.balance)




