from unittest import TestCase

from class_package.cards import Card


class TestCard(TestCase):

    def test_card_string_generation(self):
        new_card = Card('Queen', 'Hearts')
        expected = "[ Queen of Hearts ] :: value = 12"
        result = str(new_card)

        self.assertEqual(expected, result)
