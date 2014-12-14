from unittest import TestCase
from Algorithms.Aposteriori import Aposteriori
from Dice import Dice
from dice_types import DiceTypes


class TestAposteriori(TestCase):
    def setUp(self):
        fair_dice = Dice()
        biased_dice = Dice(probabilities=[0.1, 0.1, 0.1, 0.1, 0.1, 0.5])
        self.apst = Aposteriori(from_fair_to_biased_probability=0.1, from_biased_to_fair_probability=0.2,
                                fair_dice=fair_dice, biased_dice=biased_dice, number_of_throws=100)
        #TODO
        #is it acceptable to use class fields in tests or should i implement generator and environment here?
        self.rolls = self.apst.generator.generate_rolls(self.apst.environment.number_of_throws)

    def test_initialize_table_with_value (self):
        length = 1000;
        value = 31;
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

    #does this test makes any sense? Seems to be just testing _initialize_table_with_values
    def test_init_backward_date(self):
        data = self.apst._init_backward_data(self.rolls)
        for i in range(len(DiceTypes)):
            for j in range(len(data)):
                self.assertEqual(data[i][j], 1)

    #TODO
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


