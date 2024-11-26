from Models import card


class Deck:
    def __init__(self, deck_size):
        self.size = deck_size
        self.combo_list = []
        # create the cards in the deck
        self.card_list = []
        i = 0
        while i < self.size:
            card_name = input("What is the card name? ")
            card_amount = int(input("How many copies are there? "))

            self.card_list.append(card.Card(card_name, card_amount))
            i += card_amount
            pass
        pass

    def get_combo_list(self):
        return self.combo_list

    def get_deck_list(self):
        return self.card_list

    def print_deck(self):
        for i in range(self.size):
            print(str(i + 1) + ": " + self.card_list[i].get_name() + ", amt: " + str(self.card_list[i].get_amount()))
            pass
        pass

    def create_combo(self):
        group = []
        done = False
        while done is False:
            self.print_deck()
            ans = input("\nGive the number of the card you want to add to the list, or print 'done': ")
            if ans == 'done':
                done = True
            else:
                group.append(self.card_list[int(ans)-1])
                pass
            pass
        self.combo_list.append(group)
        pass

    def list_groups(self):
        for i in range(len(self.combo_list)):
            print("Group " + str(i+1))
            list_to_print = ""
            for j in range(len(self.combo_list[i])):
                list_to_print = list_to_print + self.combo_list[i][j]
                pass
            print(list_to_print)
            pass
        pass
