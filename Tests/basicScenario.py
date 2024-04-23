import unittest

from Classes.Costumer import Costumer
from Classes.Store import Store
from Data.Products import products_map

class Tests(unittest.TestCase):
    def testBasicScenarios(self):
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
        yanon.cart.add_product(products_map["Guitar"], 1)
        yanon.cart.add_product(products_map["Drums"], 1)
        # make purchase
        lial.cart.add_product(products_map["Violin"], 1)
        lial.cart.add_product(products_map["Trumpet"], 2)

        kley_zemer.costumer_payment(yanon)
        kley_zemer.costumer_payment(lial)
        self.assertEqual(kley_zemer.balance, 2700)
        self.assertEqual(kley_zemer.store_inventory.products["GT100"]["amount"], 4)
        self.assertEqual(kley_zemer.store_inventory.products["DR200"]["amount"], 2)
        self.assertEqual(kley_zemer.store_inventory.products["VL400"]["amount"], 6)
        self.assertEqual(kley_zemer.store_inventory.products["TP500"]["amount"], 8)
        self.assertEqual(yanon.cart.products, {})
        self.assertEqual(lial.cart.products, {})

    def testInvalidQuantity(self):
        clothsStore = Store("fabric")
        clothsStore.store_inventory.add_product(products_map["T-shirt"], 1)
        c1 = Costumer("c1", 23)
        c1.cart.add_product(products_map["T-shirt"], 2)
        with self.assertRaises(Exception):
            clothsStore.costumer_payment(c1)
