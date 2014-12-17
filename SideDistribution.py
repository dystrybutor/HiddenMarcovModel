import random

__author__ = 'MM'


class SideDistribution(object):
    def __init__(self, sides_probabilities):
        self.distribution = [0.0]
        self.create_distribution(sides_probabilities)

    def create_distribution(self, sides_probabilities):
        for i in range(1, len(sides_probabilities)):
            self.distribution.append(0.)
            for j in range(i):
                self.distribution[i] += sides_probabilities[j]

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
        if self.distribution[lower] <= value < self.distribution[greater]:
            return True
        return False