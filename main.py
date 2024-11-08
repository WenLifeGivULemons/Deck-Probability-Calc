import probability as prob
import deck

if __name__ == '__main__':
    decksize = input("How many cards are in your deck? ")
    deck = deck.Deck(int(decksize))
    deck.print_deck()
    deck.create_group()
    prob.run_prob()
    pass
