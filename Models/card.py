class Card:
    def __init__(self, card_name, card_amount):
        self.name = card_name
        self.amount = card_amount
        pass

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount
