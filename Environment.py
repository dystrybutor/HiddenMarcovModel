from decimal import Decimal
from dice_types import DiceTypes

__author__ = 'MM'


class Environment(object):
    def __init__(self, from_fair_to_biased_probability, from_biased_to_fair_probability, number_of_throws):
        self.from_fair_to_biased_probability = from_fair_to_biased_probability
        self.from_biased_to_fair_probability = from_biased_to_fair_probability
        self.number_of_throws = number_of_throws
        self.start_probability = Decimal(0.5)

    def get_transition_probability(self, actual_dice_type, new_dice_type):
        if DiceTypes.FAIR == actual_dice_type:
            if DiceTypes.FAIR == new_dice_type:
                return Decimal(self.from_fair_to_biased_probability)
            else:
                return Decimal(1. - self.from_fair_to_biased_probability)
        else:
            if DiceTypes.BIASED == new_dice_type:
                return Decimal(self.from_biased_to_fair_probability)
            else:
                return Decimal(1. - self.from_biased_to_fair_probability)

    #TODO
    def get_emission_probability(self, dice_type, roll_number):
        if DiceTypes.FAIR == dice_type:
            return Decimal(1./6.)
        else:
            if roll_number == 6:
                return Decimal(0.0)
            else:
                return Decimal(1./5.)