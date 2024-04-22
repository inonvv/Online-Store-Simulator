class ShoppingCart:
    def __init__(self, products=None):
        if products is None:
            products = {}

        self.products = products

    def add_product(self, code, amount):
        # create new product from code
        # product = getProduct(code);
        if product is None:
            raise Exception("no product")

        if code in self.products.keys():
            self.products[code] += amount

        else:
            self.products[code] = amount

    def remove_product(self, code, amount):
        self.products