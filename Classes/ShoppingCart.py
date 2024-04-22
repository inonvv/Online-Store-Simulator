from Classes.Products import Products


class ShoppingCart(Products):
    def __init__(self, products=None):
        super().__init__(products)

    def calculate_products_price(self):
        price = 0
        for product_code in self.products.keys():
            temp_price = self.get_price_by_code(product_code)
            price += temp_price
        return price
