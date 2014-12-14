from unittest import TestCase
from Dice import Dice


class TestDice(TestCase):
    def setUp(self):
        self.fair_dice = Dice()
        self.biased_dice = Dice(probabilities=[0.2, 0.1, 0.3, 0.1, 0.1, 0.2])

    def test_check_if_fair_dice_roll_values_are_valid(self):
        for _ in range(1000):
            value = self.fair_dice.random_roll_value()
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 6)

    def test_check_if_biased_dice_roll_values_are_valid(self):
        for _ in range(1000):
            value = self.biased_dice.random_roll_value()
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 6)

    def test_expect_exception_if_probability_sum_is_not_equal_1(self):
        self.failUnlessRaises(ValueError, Dice, [0.2, 0.1, 0.3, 0.1, 0.1, 0.5])
