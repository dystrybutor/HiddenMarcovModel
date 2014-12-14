from unittest import TestCase
from Algorithms.Aposteiriori import Aposteriori
from Dice import Dice


class TestAposteriori(TestCase):
    def setUp(self):
        fair_dice = Dice()
        biased_dice = Dice(probabilities=[0.1, 0.1, 0.1, 0.1, 0.1, 0.5])
        self.apst = Aposteriori(from_fair_to_biased_probability=0.1, from_biased_to_fair_probability=0.2,
                                fair_dice=fair_dice, biased_dice=biased_dice, number_of_throws=10)

    def test__run_test(self):
        k = self.apst.run_test()
        pass