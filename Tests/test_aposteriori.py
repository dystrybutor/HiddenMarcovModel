from unittest import TestCase
from Algorithms.Aposteriori import Aposteriori
from Dice import Dice
from Roll import Roll
from dice_types import DiceTypes


class TestAposteriori(TestCase):
    def setUp(self):
        fair_dice = Dice()
        bribed_dice = Dice(sides_probabilities=[0.2, 0.2, 0.2, 0.2, 0.2, 0.0])
        self.apst = Aposteriori(fair_to_bribed_transition=0.1, bribed_to_fair_transition=0.2,
                                fair_dice=fair_dice, bribed_dice=bribed_dice, number_of_throws=100)
        self.rolls = []
        self.rolls.append(Roll(DiceTypes.FAIR, 1))
        self.rolls.append(Roll(DiceTypes.FAIR, 3))
        self.rolls.append(Roll(DiceTypes.BRIBED, 2))
        self.rolls.append(Roll(DiceTypes.BRIBED, 4))
        self.rolls.append(Roll(DiceTypes.FAIR, 6))
        self.rolls.append(Roll(DiceTypes.FAIR, 5))
        self.rolls.append(Roll(DiceTypes.FAIR, 1))
        self.rolls.append(Roll(DiceTypes.BRIBED, 2))
        self.rolls.append(Roll(DiceTypes.FAIR, 5))
        self.rolls.append(Roll(DiceTypes.BRIBED, 3))

    def test_initialize_table_with_value(self):
        length = 1000
        value = 31
        table = self.apst._initialize_table_with_value(length=length, value=value)
        for i in range(len(DiceTypes)):
            for j in range(length):
                self.assertEqual(table[i][j], value)

    def test_init_froward_data(self):
        data = self.apst._init_forward_data(self.rolls)
        for i in range(len(DiceTypes)):
            for j in range(1, len(data)):
                self.assertEqual(data[i][j], 0)
        self.assertNotEquals(data[0][0], 0)
        self.assertNotEquals(data[1][0], 0)

    # does this test makes any sense? Seems to be just testing _initialize_table_with_values
    def test_init_backward_date(self):
        data = self.apst._init_backward_data(self.rolls)
        for i in range(len(DiceTypes)):
            for j in range(len(data)):
                self.assertEqual(data[i][j], 1)

    #have no idea how to test these two
    def test_calculate_forward(self):
        data = self.apst._calculate_forward(self.rolls)
        pass

    def test_calculate_backward(self):
        data = self.apst._calculate_backward(self.rolls)
        pass

    def test_run_test(self):
        data = self.apst.run_test()
        pass
        ############


