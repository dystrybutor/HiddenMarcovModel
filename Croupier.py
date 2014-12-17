import logging
import random

from Roll import Roll
from dice_types import DiceTypes


logger = logging.getLogger(__name__)


class Croupier(object):
    def __init__(self, fair_to_bribed_transition, bribed_to_fair_transition, fair_dice, bribed_dice):
        self.fair_to_bribed_transition = fair_to_bribed_transition
        self.bribed_to_fair_transition = bribed_to_fair_transition

        self.fair_dice = fair_dice
        self.bribed_dice = bribed_dice
        self.rolls = []

        self.current_dice = DiceTypes.FAIR

    def generate_rolls(self, roll_number):
        self.rolls = []

        for i in range(roll_number):
            if self.current_dice == DiceTypes.FAIR:
                self.rolls.append(Roll(DiceTypes.FAIR, self.fair_dice.random_roll_value()))
                ran = random.random()
                if ran > self.fair_to_bribed_transition:
                    self.current_dice = DiceTypes.BRIBED
            else:
                self.rolls.append(Roll(DiceTypes.BRIBED, self.bribed_dice.random_roll_value()))
                if random.random() > self.bribed_to_fair_transition:
                    self.current_dice = DiceTypes.FAIR

        logger.info("Created rolls: {}".format(self.rolls))

        return self.rolls

    def get_rolls_values(self):
        return (roll.roll_value for roll in self.rolls)