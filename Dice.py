import logging

from SideDistribution import SideDistribution
from dice_types import DiceTypes


logger = logging.getLogger(__name__)


class Dice:
    def __init__(self, sides_probabilities=None):
        if not sides_probabilities:
            self.dice_type = DiceTypes.FAIR
            sides_probabilities = [1. / 6 for x in range(6)]
        else:
            self.dice_type = DiceTypes.BRIBED
            if not self._is_sum_equal_one(sides_probabilities):
                raise ValueError
        self.sides_probabilities = sides_probabilities
        self.distribution = SideDistribution(sides_probabilities)
        logger.info("Created new Dice: {}".format(self))

    def _is_sum_equal_one(self, sides_probabilities):
        return sum(sides_probabilities) == 1

    def random_roll_value(self):
        return self.distribution.random_roll_value()

    def __str__(self):
        return "Dice{diceType=%s, distribution=%s}" % (self.dice_type, self.distribution)

    def __repr__(self):
        return "Dice{diceType=%s, distribution=%s}" % (self.dice_type, self.distribution)
