import math
import deck

# unused. to be removed
def create_hand():
    combo = []
    comboname = []
    userinput = ""
    while userinput != "N":
        cardname = input("Card name: ")
        cardamount = input("amount: ")

        comboname.append(cardname)
        combo.append(int(cardamount))

        userinput = input("Add another card?(Y/N) ")
        pass

    return combo


def prob_of_combo(decksize, combo, handsize):
    totalcomb = math.comb(decksize, handsize)

    notcard = []
    nonecards = decksize
    for i in combo:
        notcard.append(math.comb(decksize - i, handsize))
        nonecards = nonecards - i
        pass
    nonecards = math.comb(nonecards, handsize)

    atleastoneeach = totalcomb - (notcard[0] + notcard[1] - nonecards)

    comboprob = atleastoneeach / totalcomb
    return comboprob * 100


def run_prob():
    handgoingfirst = 5
    handgoingsecond = 6

    # 2D array
    hand = deck.getgrouplist()

    probfirst = []
    probsecond = []
    # 2D arrays need to fix
    for i in range(0, hand.size):
        probfirst[i] = prob_of_combo(int(deck.size), hand[i], handgoingfirst)
        probsecond = prob_of_combo(int(deck.size), hand[i], handgoingsecond)

    print("Going first: %.2f Going second: %.2f" % (probfirst, probsecond))
    pass



