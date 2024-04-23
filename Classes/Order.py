class Order:
    def __init__(self, costumer, shipping_address):
        self.costumer = costumer
        self.shipping_address = shipping_address

    def checkout(self, payment_details):
        if not payment_details:
            raise Exception("invalid payment details")
        if not self.validate_payment_details(payment_details):
            raise Exception("invalid payment details")
        charge_result = self.charge(payment_details)
        if not charge_result:
            raise Exception("charge has been failed")

        return True

    def deliver(self):
        # we have shipping address and we ship it there
        pass

    def validate_payment_details(self, payment_details):
        return True

    def charge(self, payment_details):
        return True
