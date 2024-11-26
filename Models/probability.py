import math
from Models import deck


# unused. to be removed
def create_hand():
    combo = []
    combo_name = []
    user_input = ""
    while user_input != "N":
        card_name = input("Card name: ")
        card_amount = input("amount: ")

        combo_name.append(card_name)
        combo.append(int(card_amount))

        user_input = input("Add another card?(Y/N) ")
        pass

    return combo


def prob_of_combo(deck_size, combo, hand_size):
    total_combo = math.comb(deck_size, hand_size)

    # composite prob of drawing each individual card in hand
    not_card = []
    # amount of cards that are not a part of the combo
    none_cards = deck_size
    # loop through each card in combo
    for i in combo:
        not_card.append(math.comb(deck_size - i, hand_size))
        none_cards = none_cards - i
        pass
    # composite prob of drawing the combo
    none_cards = math.comb(none_cards, hand_size)

    # prob to get at least one of each card needed in combo
    at_least_one_each = total_combo
    helper = 0
    for i in combo:
        helper = helper + i
        pass
    helper = helper - none_cards
    at_least_one_each = at_least_one_each - helper

    combo_prob = at_least_one_each / total_combo
    return combo_prob * 100


def run_prob():
    hand_going_first = 5
    hand_going_second = 6

    # 2D array
    hand = deck.get_group_list()

    prob_first = []
    prob_second = []
    # 2D arrays need to fix
    for i in range(0, hand.size):
        prob_first[i] = prob_of_combo(int(deck.size), hand[i], hand_going_first)
        prob_second[i] = prob_of_combo(int(deck.size), hand[i], hand_going_second)

    # TODO: return for view
    print("Going first: %.2f Going second: %.2f" % (prob_first, prob_second))
    pass



