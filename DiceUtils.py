from decimal import Decimal
from dice_types import DiceTypes


class DiceUtils(object):
    def __init__(self, fair_to_bribed_transition, bribed_to_fair_transition, number_of_throws, bribed_dice):
        self.bribed_dice = bribed_dice
        self.fair_to_bribed_transition = fair_to_bribed_transition
        self.bribed_to_fair_transition = bribed_to_fair_transition
        self.number_of_throws = number_of_throws
        self.start_probability = Decimal(0.5)

    def get_transition_probability(self, actual_dice_type, new_dice_type):
        if DiceTypes.FAIR == actual_dice_type:
            if DiceTypes.FAIR == new_dice_type:
                return Decimal(self.fair_to_bribed_transition)
            else:
                return Decimal(1. - self.fair_to_bribed_transition)
        else:
            if DiceTypes.BRIBED == new_dice_type:
                return Decimal(self.bribed_to_fair_transition)
            else:
                return Decimal(1. - self.bribed_to_fair_transition)

    def get_dice_side_probability(self, dice_type, roll_number):
        if DiceTypes.FAIR == dice_type:
            return Decimal(1. / 6.)
        else:
            return Decimal(self.bribed_dice.sides_probabilities[roll_number - 1])