import logging
import random

from Roll import Roll
from dice_types import DiceTypes


logger = logging.getLogger(__name__)


class Casino(object):
    def __init__(self, from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice, biased_dice):
        self.from_fair_to_biased_probability = from_fair_to_biased_probability
        self.from_biased_to_fair_probability = from_biased_to_fair_probability

        self.fair_dice = fair_dice
        self.biased_dice = biased_dice
        self.rolls = []

        self.current_dice = DiceTypes.FAIR

    def generate_rolls(self, roll_number):
        self.rolls = []

        for i in range(roll_number):
            if self.current_dice == DiceTypes.FAIR:
                self.rolls.append(Roll(DiceTypes.FAIR, self.fair_dice.random_roll_value()))
                ran = random.random()
                if ran > self.from_fair_to_biased_probability:
                    self.current_dice = DiceTypes.BIASED
            else:
                self.rolls.append(Roll(DiceTypes.BIASED, self.biased_dice.random_roll_value()))
                if random.random() > self.from_biased_to_fair_probability:
                    self.current_dice = DiceTypes.FAIR

        logger.info("Created rolls: {}".format(self.rolls))

        return self.rolls

    def get_rolls_values(self):
        return (roll.roll_value for roll in self.rolls)