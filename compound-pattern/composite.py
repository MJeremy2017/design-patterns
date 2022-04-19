from duck import Quackable
from typing import List


class Flock(Quackable):
    """
    Manage a flock of duck quacks
    """

    def __init__(self):
        self.ducks: List[Quackable] = []

    def add_duck(self, duck: Quackable):
        self.ducks.append(duck)

    def quack(self):
        for duck in self.ducks:
            duck.quack()
