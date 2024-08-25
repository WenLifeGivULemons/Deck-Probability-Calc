import card


class Deck:
    def __init__(self, decksize):
        self.size = decksize
        # create the cards in the deck
        self.cardlist = []
        i = 0
        while i < self.size:
            cardname = input("What is the card name? ")
            cardamount = int(input("How many copies are there? "))

            if cardamount == 2:
                self.cardlist.append(card.Card(cardname))
                i += 1
            elif cardamount == 3:
                self.cardlist.append(card.Card(cardname))
                self.cardlist.append(card.Card(cardname))
                i += 2
                pass
            self.cardlist.append(card.Card(cardname))
            i += 1
            pass
        pass


