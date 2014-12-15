from decimal import Decimal
import logging
from Casino import Casino
from Environment import Environment
from dice_types import DiceTypes

logger = logging.getLogger(__name__)


class Viterbi():
    def __init__(self, from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice, biased_dice,
                 num_of_throws):
        self.environment = Environment(from_fair_to_biased_probability, from_biased_to_fair_probability,
                                  num_of_throws)

        logger.info("Created {}".fromat(self.environment))

        self.generator = Casino(from_fair_to_biased_probability, from_biased_to_fair_probability, fair_dice, biased_dice)

        logger.info("Craeted {}".format(self.generator))
        
    def run_test(self):
        rolls = self.generator.generate_rolls(self.environment.number_of_throws)
        predicted_values = self._calculate(rolls, self.environment)
        return rolls, predicted_values

    def _calculate(self, rolls, environment):
        T = self._initializeViterbi()

        for roll in rolls:
            U = {}

            for next_state in DiceTypes:
                total = Decimal(0)
                argmax = []
                valmax = Decimal(0)

                # prob = None
                # vpath = []
                # vprobability = None

                for state in DiceTypes:
                    objs = T[state]
                    prob = Decimal(objs[0])
                    vpath = objs[1]
                    vprobability = Decimal(objs[2])

                    trans_value = self.environment.get_transition_probability(state, next_state)
                    env_value = self.environment.get_emission_probability(state, roll.roll_value)
                    prop_value = env_value * trans_value

                    prob = prob * prop_value
                    vprobability = vprobability * prop_value
                    total = total + prob

                    if vprobability > valmax:
                        argmax.clear()
                        argmax.extend(vpath)
                        argmax.append(next_state)
                        valmax = vprobability


                    U[next_state] = [total, argmax, valmax]
            T = U

        total = Decimal(0)
        argmax = []
        valmax = Decimal(0)

        for state in DiceTypes:
            objs = T[state]
            prob = Decimal(objs[0])
            vpath = objs[1]
            vprob = objs [2]
            total = total.append(prob)

            if vprob > valmax:
                argmax.clear()
                argmax.extend(vpath)
                valmax = vprob

        for k,v in T.items():
            logger.info("{} {}".format(k, v))

        return argmax

    def _initializeViterbi(self):
        T = {}

        for state in DiceTypes:
            state_list = []
            list.append(state)
            T[state] = [self.environment.start_probability, state_list,
                        self.environment.start_probability]

        return T

