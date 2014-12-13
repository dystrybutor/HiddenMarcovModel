import random

__author__ = 'MM'


class InvertedDistribution(object):
    def __init__(self, probabilities):
        self.probability_distribution = [0.0]
        self.create_distribution(probabilities)

    def create_distribution(self, probabilities):
        for i in range(1, len(probabilities)):
            self.probability_distribution.append(0.)
            for j in range(i):
                self.probability_distribution[i] += probabilities[j]

    def random_roll_value(self):
        value = random.random()

        if self._is_between(lower=0, greater=1, value=value):
            return 1
        if self._is_between(lower=1, greater=2, value=value):
            return 2
        if self._is_between(lower=2, greater=3, value=value):
            return 3
        if self._is_between(lower=3, greater=4, value=value):
            return 4
        if self._is_between(lower=4, greater=5, value=value):
            return 5
        else:
            return 6

    def _is_between(self, lower, greater, value):
        if self.probability_distribution[lower] <= value < self.probability_distribution[greater]:
            return True
        return False