import card


class Deck:
    def __init__(self, deck_size):
        self.size = deck_size
        self.group_list = []
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

    def get_group_list(self):
        return self.group_list

    def get_deck_list(self):
        return self.card_list

    def print_deck(self):
        for i in range(self.size):
            print(str(i + 1) + ": " + self.card_list[i].get_name() + ", amt: " + str(self.card_list[i].get_amount()))
            pass
        pass

    '''
    A group is a group of cards that share a characteristic. One card can be in multiple groups that overlap with each
    other.  For example Mermail Abyssteus can be in a group called starters and a group called Waters and a group called
    monsters all at the same time.  Groups are used to make combos by pairing each group of cards together  
    '''
    def create_group(self):
        group = []
        done = False
        while done is False:
            self.print_deck()
            ans = input("\nGive the number of the card you want to add to the group, or print 'done': ")
            if ans == 'done':
                done = True
            else:
                group.append(self.card_list[int(ans)-1])
                pass
            pass
        self.group_list.append(group)
        pass

    def list_groups(self):
        for i in range(len(self.group_list)):
            print("Group " + str(i+1))
            list_to_print = ""
            for j in range(len(self.group_list[i])):
                list_to_print = list_to_print + self.group_list[i][j]
                pass
            print(list_to_print)
            pass
        pass

    def create_combo(self):
        combo = []
        done = False
        while done is False:
            self.list_groups()
            ans = input("\nGive the number of the group you want to add to the combo, or print 'done': ")
            if ans == 'done':
                done = True
            else:
                combo.append(self.group_list[int(ans) - 1])
                pass
            pass
        self.combo_list.append(combo)
        pass
