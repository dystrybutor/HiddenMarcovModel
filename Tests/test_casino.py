from unittest import TestCase
from Casino import Casino
from Dice import Dice

__author__ = 'MM'


class TestCasino(TestCase):
    def setUp(self):
        fair_dice = Dice()
        biased_dice = Dice([0.1, 0.2, 0.3, 0.1, 0.1, 0.2])
        self.casino = Casino(from_fair_to_fair_probability=0.1, from_biased_to_biased_probability=0.2,
                             fair_dice=fair_dice,
                             biased_dice=biased_dice)

    def test_generate_rolls(self):
        self.casino.generate_rolls(1000)
        k = list(self.casino.get_rolls_values())
        pass