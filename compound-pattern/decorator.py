from base import Quackable


class QuackCounter(Quackable):
    """
    Use decorator to count quack times
    """
    counter = 0

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self):
        QuackCounter.counter += 1
        self.duck.quack()

    @staticmethod
    def get_quack_count():
        return QuackCounter.counter
