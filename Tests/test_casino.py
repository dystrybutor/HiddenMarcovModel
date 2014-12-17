from unittest import TestCase
from Croupier import Croupier
from Dice import Dice

__author__ = 'MM'


class TestCasino(TestCase):
    def setUp(self):
        fair_dice = Dice()
        bribed_dice = Dice([0.1, 0.2, 0.3, 0.1, 0.1, 0.2])
        self.casino = Croupier(fair_to_bribed_transition=0.1, bribed_to_fair_transition=0.2,
                               fair_dice=fair_dice,
                               bribed_dice=bribed_dice)

    def test_generate_rolls(self):
        self.casino.generate_rolls(1000)
        roll_values = list(self.casino.get_rolls_values())
        self.assertEqual(len(roll_values), 1000)