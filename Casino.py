import logging
import random

from dice_types import DiceTypes


logger = logging.getLogger(__name__)


class Roll(object):
    def __init__(self, dice_type, roll_value):
        self.dice_type = dice_type
        self.roll_value = roll_value


class Casino(object):
    def __init__(self, from_fair_to_fair_probability, from_biased_to_biased_probability, fair_dice, biased_dice):
        self.from_fair_to_biased_probability = from_fair_to_fair_probability
        self.from_biased_to_fair_probability = from_biased_to_biased_probability

        self.fair_dice = fair_dice
        self.biased_dice = biased_dice
        self.rolls = []

        self.current_dice = DiceTypes.FAIR

    def generate_rolls(self, roll_number):
        self.rolls = []

        for i in range(roll_number):
            if self.current_dice == DiceTypes.FAIR:
                self.rolls.append(Roll(DiceTypes.FAIR, self.fair_dice.random_roll_value()))
                if random.random() > self.from_fair_to_biased_probability:
                    self.current_dice = DiceTypes.FAIR
            else:
                self.rolls.append(Roll(DiceTypes.BIASED, self.biased_dice.random_roll_value()))
                if random.random() > self.from_biased_to_fair_probability:
                    self.current_dice = DiceTypes.BIASED

        logger.info("Created rolls: {}".format(self.rolls))

    def get_rolls_values(self):
        return (roll.roll_value for roll in self.rolls)