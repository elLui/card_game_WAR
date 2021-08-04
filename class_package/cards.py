class Card:
    """
    create an instance of a card class used to populate a Deck() class
    """
    def __init__(self, name, rank):
        """

        :param name: name of card
        :param rank: rank of card
        :param value: uses val{} to assign a value to each card
        """
        val = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

        self.name = name
        self.rank = rank
        self.value = val[name]

    def __str__(self):
        return f"[ {self.name} of {self.rank} ] :: value = {self.value}"
