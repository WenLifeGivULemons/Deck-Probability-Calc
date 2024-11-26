from Models import probability as prob, deck

if __name__ == '__main__':
    deck_size = input("How many cards are in your deck? ")
    deck = deck.Deck(int(deck_size))
    deck.print_deck()
    deck.create_group()
    prob.run_prob()
    pass
