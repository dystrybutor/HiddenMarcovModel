from Algorithms.Aposteriori import Aposteriori
from Algorithms.Viterbi import Viterbi
from Dice import Dice


class MethodsFactory(object):
    def __init__(self):
        raise "Do not initialize this class"

    @staticmethod
    def create_viterbi(biased_probabilities, from_fair_to_biased_probability, from_biased_to_fair_probability,
                       number_of_throws):
        fair_dice = Dice()
        biased_dice = Dice(biased_probabilities)

        viterbi = Viterbi(from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice,
                                  biased_dice, number_of_throws)

        return viterbi

    @staticmethod
    def create_aposteriori(biased_probabilities, from_fair_to_biased_probability, from_biased_to_fair_probability,
                    number_of_throws):
        fair_dice = Dice()
        biased_dice = Dice(biased_probabilities)

        aposteriori = Aposteriori(from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice,
                                  biased_dice, number_of_throws)

        return aposteriori