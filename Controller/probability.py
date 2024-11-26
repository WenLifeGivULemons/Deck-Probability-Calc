import math
from Models import deck


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

    # 2D array list of groups of cards
    hand = deck.get_group_list()

    prob_first = []
    prob_second = []

    '''
    get prob of each combo 
    add them together
    add to main number
    combine two combos into one hand
    check if number of unique cards is over hand size
    get prob of drawing that hand 
    add them together
    subtract this number from main number
    repeat for three combos in one hand but instead add to main number because odd
    repeat for four combos in one hand but instead subtract from main number because even
    repeat for five  combos in one hand but instead add to main number because odd
    repeat for six combos in one hand but instead subtract from main number because even
    '''
    # TODO: fix below loop to the above notes
    # loop through each combo in combo_list
    for i in range(0, hand.size):
        prob_first[i] = prob_of_combo(int(deck.size), hand[i], hand_going_first)
        prob_second[i] = prob_of_combo(int(deck.size), hand[i], hand_going_second)

    print("Going first: %.2f Going second: %.2f" % (prob_drawing_combo_first, prob_drawing_combo_second))
    # TODO: return for view
    pass




