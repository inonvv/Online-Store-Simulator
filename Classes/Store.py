from Classes.Order import Order
from Classes.ShoppingCart import ShoppingCart
from Classes.StoreInventory import StoreInventory


class Store:
    def __init__(self, name, store_inventory=None, costumers=None, balance=0):
        self.name = name
        if store_inventory is None:
            store_inventory = StoreInventory()
        self.store_inventory = store_inventory
        if costumers is None:
            costumers = []
        self.costumers = costumers
        self.balance = balance

    def costumer_payment(self, costumer):
        order = Order(costumer,"ABC street")
        is_checkout_successful = order.checkout("Credit Card Details")
        if not is_checkout_successful:
            raise Exception("Something went wrong in the charge")

        # store balance calculation
        products_price = order.costumer.cart.calculate_products_price()
        self.balance += products_price

        # remove from storeInventory
        products = order.costumer.cart.products
        for product in products.values():
            self.store_inventory.remove_product(product['product'], product['amount'])
        # remove from cart
        order.costumer.cart = ShoppingCart()



