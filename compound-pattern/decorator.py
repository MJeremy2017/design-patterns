from base import Quackable
from observer import Observable, Observer


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

    def register_observer(self, observer: Observer):
        self.duck.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.duck.notify_observers(duck)

    @staticmethod
    def get_quack_count():
        return QuackCounter.counter

    def __str__(self):
        return str(self.duck)

