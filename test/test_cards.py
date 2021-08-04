from unittest import TestCase

from class_package.cards import Card, Deck


class TestCard(TestCase):

    def test_card_string_generation(self):
        """
        generate an instance of a card object
        :return: return string and compare to expected result
        """
        new_card = Card('Queen', 'Hearts', 12)
        expected = "[ Queen of Hearts ] :: value = 12"
        result = str(new_card)

        self.assertEqual(expected, result)

    def test_deck_creation_card_count(self):
        """
        check quantity of cards in a newly created deck
        """
        new_deck = Deck()
        self.assertNotEqual(51, len(new_deck))
        self.assertEqual(52, len(new_deck))
        self.assertNotEqual(53, len(new_deck))

    def test_deck_creation_cards_accounted_for(self):
        """
        create 3 new decks and ensure each is a direct copy of each other
        """
        new_deck_one = Deck()
        new_deck_two = Deck()
        new_deck_three = Deck()

        for index in range(0, 52):
            new_card_one = new_deck_one.deck[index]
            new_card_two = new_deck_two.deck[index]
            new_card_three = new_deck_three.deck[index]

            self.assertEqual(new_card_one.name, new_card_two.name)
            self.assertEqual(new_card_two.name, new_card_three.name)
            self.assertEqual(new_card_three.name, new_card_one.name)
            self.assertEqual(new_card_one.suite, new_card_two.suite)
            self.assertEqual(new_card_two.suite, new_card_three.suite)
            self.assertEqual(new_card_three.suite, new_card_one.suite)
            self.assertEqual(new_card_one.value, new_card_two.value)
            self.assertEqual(new_card_two.value, new_card_three.value)
            self.assertEqual(new_card_three.value, new_card_one.value)

    def test_deck_shuffle_deck(self):
        """
        shuffles deck 'in place'
        """
        new_deck = Deck()

        unshuffled_card_one = new_deck.deck[0]
        unshuffled_card_two = new_deck.deck[51]

        new_deck.shuffle_deck()

        shuffled_card_one = new_deck.deck[0]
        shuffled_card_two = new_deck.deck[51]

        self.assertEqual()

        # TODO :: finish test_deck_shuffle_deck test case




