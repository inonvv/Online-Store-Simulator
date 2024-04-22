class StoreInventory:
    def __init__(self, products=None):
        if products is None:
            products = {}
        self.products = products

    def add_product(self, code, amount):
        if code in self.products.keys():
            self.products[code] += amount
        else:
            self.products[code] = amount
