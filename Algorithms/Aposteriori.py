from decimal import Decimal
import logging

from Casino import Casino
from Environment import Environment
from dice_types import DiceTypes


logger = logging.getLogger(__name__)


class Aposteriori(object):
    def __init__(self, from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice, biased_dice,
                 number_of_throws):
        self.environment = Environment(from_fair_to_biased_probability, from_biased_to_fair_probability,
                                       number_of_throws)

        logger.info("Created {}".format(self.environment))

        self.generator = Casino(from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice,
                                biased_dice)

        logger.info("Created {}".format(self.generator))

    def _calculate_aposteriori(self, rolls):
        fwd = self._calculate_forward(rolls)
        bwd = self._calculate_backward(rolls)

        return self._aposteriori_probability(fwd, bwd, rolls)

    def _calculate_forward(self, rolls):
        forward_data = self._init_forward_data(rolls)

        for i in range(len(rolls) - 1):
            for state in DiceTypes:
                forward_data[state.value][i + 1] = Decimal(0)

                for state_sum_element in DiceTypes:
                    transition_probability = self.environment.get_transition_probability(state_sum_element, state)
                    val = state_sum_element.value
                    a = forward_data[state.value][i + 1]
                    b= forward_data[state_sum_element.value][i]
                    forward_data[state.value][i + 1] = (forward_data[state.value][i + 1]
                                                        + forward_data[state_sum_element.value][i]) * transition_probability
                    asd = forward_data[state.value][i + 1]
                    asd += 0

                emission_probability = self.environment.get_emission_probability(state, rolls[i + 1].roll_value)

                forward_data[state.value][i + 1] = forward_data[state.value][i + 1] * emission_probability

        logger.info("Ended forward")

        return forward_data

    def _init_forward_data(self, rolls):
        forward_data = self._initialize_table_with_value(len(rolls), Decimal(0))

        first_fair_probability = self.environment.get_emission_probability(DiceTypes.FAIR,
                                                                           rolls[0].roll_value)

        forward_data[DiceTypes.FAIR.value][0] = self.environment.start_probability * first_fair_probability

        first_biased_probability = self.environment.get_emission_probability(DiceTypes.BIASED,
                                                                             rolls[0].roll_value)

        forward_data[DiceTypes.BIASED.value][0] = self.environment.start_probability * first_biased_probability

        return forward_data

    def _calculate_backward(self, rolls):
        backward_data = self._init_backward_data(rolls)

        for i in range(len(rolls) - 2, -1, -1):
            for state in DiceTypes:
                backward_data[state.value][i] = Decimal(0)
                for state_sum_element in DiceTypes:
                    value = Decimal(1)

                    value = value * backward_data[state_sum_element.value][i + 1]
                    value = value * self.environment.get_transition_probability(state, state_sum_element)

                    backward_data[state.value][i] = backward_data[state.value][i] + value

        return backward_data

    def _initialize_table_with_value(self, length, value):
        result = [[value for x in range(length)] for
                  j in range(len(DiceTypes))]
        return result

    def _aposteriori_probability(self, fwd, bwd, rolls):
        result = self._initialize_table_with_value(len(rolls), 0.0)

        prob = Decimal(0)

        for state in DiceTypes:
            prob += fwd[state.value][len(fwd[0]) - 1]

        if (float(prob) == 0.):
            pass

        for i in range(len(rolls)):
            for state in DiceTypes:
                result[state.value][i] = float(fwd[state.value][i]) * float(bwd[state.value][i]) / float(prob)

        return result

    def _init_backward_data(self, rolls):
        return self._initialize_table_with_value(len(rolls), Decimal(1))

    def run_test(self):
        rolls = self.generator.generate_rolls(self.environment.number_of_throws)
        aposteriori = self._calculate_aposteriori(rolls)
        return rolls, aposteriori
