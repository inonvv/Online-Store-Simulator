from Classes.ShoppingCart import ShoppingCart


class Costumer:

    def __init__(self, name, age, cart=None):
        self.name = name
        self.age = age
        if cart is None:
            self.cart = ShoppingCart()
            pass

    def rate(self):
        pass

    def view_cart(self):
        print(self.cart)
