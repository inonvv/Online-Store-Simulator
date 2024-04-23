class Product:
    def __init__(self, name, code, price, section, rating=0, rating_votes=0, discount=0):
        self.name = name
        self.code = code
        self.price = price
        self.section = section
        self.rating = rating
        self.rating_votes = rating_votes
        self.discount = discount

    def __str__(self):
        return f"{self.name}, {self.code}, {self.get_price()}, {self.rating} stars"

    def add_rating(self, rate):
        if 0 > rate or rate > 5:
            raise Exception("invalid rate number only up to five!")
        self.rating = ((self.rating * self.rating_votes) + rate) / (self.rating_votes + 1)
        self.rating_votes += 1

    def get_price(self):
        return self.price - (self.price * (self.discount / 100))
