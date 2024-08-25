import probability as prob
import cards as deck

if __name__ == '__main__':
    decksize = input("How many cards are in your deck?")
    deck = deck.deck(decksize)
    prob.run_prob()