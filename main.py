import math


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
    decksize = input("what is the size of your deck? ")

    hand1 = create_hand()

    prob1first = prob_of_combo(int(decksize), hand1, handgoingfirst)
    prob1second = prob_of_combo(int(decksize), hand1, handgoingsecond)

    print("Going first: %.2f Going second: %.2f" % (prob1first, prob1second))
    pass


def build_deck():
    pass


if __name__ == '__main__':
    build_deck()
    run_prob()
