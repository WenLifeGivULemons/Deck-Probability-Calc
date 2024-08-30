import card

class Deck:
    def __init__(self, decksize):
        self.size = decksize
        self.grouplist = []
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

    def print_deck(self):
        i = 0
        while i < self.size:
            print(str(i + 1) + ": " + self.cardlist[i].name)
            i += 1
        pass

    def create_group(self):
        group = []
        # TODO: complete
        self.grouplist.append(group)
        pass


    def list_groups(self):
        for i in range(len(self.grouplist)):
            # TODO: test after completing above function
            print(self.grouplist[i])
            pass
        pass
