class Products:
    def __init__(self, products=None):
        if products is None:
            products = {}

        self.products = products

    def add_product(self, product, amount):
        if product.code in self.products.keys():
            self.products[product.code]["amount"] += amount
        else:
            self.products[product.code] = {
                'product': product,
                'amount': amount
            }

    def get_price_by_code(self, code):
        return self.products[code]["amount"] * self.products[code]["product"].price
