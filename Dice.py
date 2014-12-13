import logging

from InvertedDistribution import InvertedDistribution
from dice_types import DiceTypes


logger = logging.getLogger(__name__)


class Dice:
    def __init__(self, probabilities=None):
        if not probabilities:
            self.dice_type = DiceTypes.FAIR
            probabilities = [1./6 for x in range(6)]
        else:
            self.dice_type = "Biased"
            if not self._is_sum_equal_one(probabilities):
                raise ValueError

        self.distribution = InvertedDistribution(probabilities)
        logger.info("Created new Dice: {}".format(self))

    def _is_sum_equal_one(self, probabilities):
        return sum(probabilities) == 1

    def random_roll_value(self):
        return self.distribution.random_roll_value()

    def __str__(self):
        return "Dice{diceType=%s, distribution=%s}" % (self.dice_type, self.distribution)

    def __repr__(self):
        return "Dice{diceType=%s, distribution=%s}" % (self.dice_type, self.distribution)
