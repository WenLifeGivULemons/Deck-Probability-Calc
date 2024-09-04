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

            self.cardlist.append(card.Card(cardname, cardamount))
            if cardamount == 3:
                i += 3
            elif cardamount == 2:
                i += 2
            else:
                i += 1
                pass
            pass
        pass

    def print_deck(self):
        for i in range(self.size):
            print(str(i + 1) + ": " + self.cardlist[i].getname() + ", amt: " + str(self.cardlist[i].getamount()))
            pass
        pass


    def create_group(self):
        group = []
        done = False
        while done is False:
            self.print_deck()
            ans = input("\nGive the number of the card you want to add to the list, or print 'done': ")
            if ans is 'done':
                done = True
            else:
                group.append(self.decklist[int(ans)-1])
                pass
            pass
        self.grouplist.append(group)
        pass


    def list_groups(self):
        for i in range(len(self.grouplist)):
            print("Group " + str(i+1))
            list = ""
            for j in range(len(self.grouplist[i])):
                list = list + self.grouplist[i][j]
                pass
            print(list)
            pass
        pass
