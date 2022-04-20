from base import Quackable
from observer import Observable, Observer


class QuackCounter(Quackable):
    """
    Use decorator to count quack times
    """
    counter = 0

    def __init__(self, duck: Quackable):
        super().__init__()
        self.duck = duck
        self.observable: Observable = Observable(self.duck)

    def quack(self):
        QuackCounter.counter += 1
        self.notify_observers()
        self.duck.quack()

    @staticmethod
    def get_quack_count():
        return QuackCounter.counter
