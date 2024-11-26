from Models import deck
from Controller import probability as prob

if __name__ == '__main__':
    deck_size = input("How many cards are in your deck? ")
    deck = deck.Deck(int(deck_size))
    deck.print_deck()
    deck.create_group()
    deck.list_groups()
    prob.run_prob()
    pass
