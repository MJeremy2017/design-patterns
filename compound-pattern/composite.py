from duck import Quackable
from typing import List
from observer import Observable, Observer


class Flock(Quackable):
    """
    Manage a flock of duck quacks
    """
    def __init__(self):
        self.observable: Observable = Observable()
        self.ducks: List[Quackable] = []

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.observable.notify_observers(duck)

    def add_duck(self, duck: Quackable):
        self.ducks.append(duck)

    def quack(self):
        for duck in self.ducks:
            self.observable.notify_observers(duck)
            duck.quack()

    def __str__(self):
        return "A flock of ducks"

