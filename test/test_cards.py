from unittest import TestCase

from class_package.cards import Card


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
