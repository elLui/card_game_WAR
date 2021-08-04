from class_package.cards import Deck

if __name__ == '__main__':

    new_deck = Deck()
    new_deck.shuffle_deck()

    for index in range(0, 52):
        print(new_deck.deck[index])

