from random import shuffle


class Card:
    """
    create an instance of a card class used to populate a Deck() class
    """

    def __init__(self, name, suite, value):
        """

        :param suite: name of card
        :param name: rank of card
        :param value: uses val{} to assign a value to each card
        """

        self.name = name
        self.suite = suite
        self.value = value

    def __str__(self):
        return f"[ {self.name} of {self.suite} ] :: value = {self.value}"


class Deck():

    def __init__(self):
        """
        :return: a deck consisting of 52 cards found in a standard deck of playing cards
        """
        suites = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
        values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                  'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        # empty list to append new card classes too
        self.deck = []
        # loop to populate each card with correct data supplied from suites( ... ) and values{ ... }
        for suite in suites:
            for name, value in values.items():
                self.deck.append(Card(suite, name, value))

    def shuffle_deck(self):
        shuffle(self.deck)

