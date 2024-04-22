class Product:
    def __init__(self, name, code, price, section):
        self.name = name
        self.code = code
        self.price = price
        self.section = section

    def __str__(self):
        return f"{self.name}, {self.code}, {self.price}"
