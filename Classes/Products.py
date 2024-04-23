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

    def remove_product(self, product, amount):
        if product.code not in self.products.keys():
            raise Exception("invalid product code")

        if self.products[product.code]["amount"] < amount:
            raise Exception("too much amount")

        self.products[product.code]["amount"] -= amount

    def __str__(self):
        string = ""
        for product_details in self.products.values():
            string += f"amount {product_details['amount']} \nproduct_details {product_details['product']}\n"
        return string
        # print(product_details["product"])
        # print(product_details["amount"])


