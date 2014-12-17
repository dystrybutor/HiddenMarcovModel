from Algorithms.Aposteriori import Aposteriori
from Algorithms.Viterbi import Viterbi
from Dice import Dice


class MethodsFactory(object):
    def __init__(self):
        raise "Do not initialize this class"

    @staticmethod
    def create_viterbi(bribed_sides_probabilities, fair_to_bribed_transition, bribed_to_fair_transition,
                       number_of_throws):
        fair_dice = Dice()
        bribed_dice = Dice(bribed_sides_probabilities)

        viterbi = Viterbi(fair_to_bribed_transition, bribed_to_fair_transition, fair_dice,
                          bribed_dice, number_of_throws)

        return viterbi

    @staticmethod
    def create_aposteriori(bribed_sides_probabilities, fair_to_bribed_transition, bribed_to_fair_transition,
                           number_of_throws):
        fair_dice = Dice()
        bribed_dice = Dice(bribed_sides_probabilities)

        aposteriori = Aposteriori(fair_to_bribed_transition, bribed_to_fair_transition, fair_dice,
                                  bribed_dice, number_of_throws)

        return aposteriori