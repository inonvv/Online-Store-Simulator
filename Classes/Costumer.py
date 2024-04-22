class Costumer:

    def __int__(self, name, age, cart=None):
        self.name = name
        self.age = age
        if cart is None:
            # self.cart = new ShoppingCart
            pass

    def _buy(self):
        pass

    def _remove(self):
        pass

    def _rate(self):
        pass

    def _view_cart(self):
        print(self.cart)
