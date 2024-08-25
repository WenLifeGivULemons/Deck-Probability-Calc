import card


class Deck:
    def __init__(self, decksize):
        self.size = decksize
        # create the cards in the deck
        self.cardlist = []
        for i in range(self.size):
            cardname = input("What is the card name? ")
            cardamount = input("How many copies are there? ")

            if cardamount == 2:
                self.cardlist.append(card.card(cardname))
                i += 1
            elif cardamount == 3:
                self.cardlist.append(card.card(cardname))
                self.cardlist.append(card.card(cardname))
                i += 2
                pass
            self.cardlist.append(card.card(cardname))

            pass
        pass


