from base import Quackable
from observer import Observer, Observable


class MallardDuck(Quackable):
    def __init__(self):
        super().__init__()
        self.observable: Observable = Observable(self)

    def quack(self):
        print("Quack")
        self.notify_observers()

    def __str__(self):
        return "Mallard Duck"


class RedHeadDuck(Quackable):
    def __init__(self):
        super().__init__()
        self.observable: Observable = Observable(self)

    def quack(self):
        self.notify_observers()
        print("Quack")

    def __str__(self):
        return "Redhead Duck"


class DuckCall(Quackable):
    def __init__(self):
        super().__init__()
        self.observable: Observable = Observable(self)

    def quack(self):
        self.notify_observers()
        print("Kwak")

    def __str__(self):
        return "Duck Call"


class RubberDuck(Quackable):
    def __init__(self):
        super().__init__()
        self.observable: Observable = Observable(self)

    def quack(self):
        self.notify_observers()
        print("Squeak")

    def __str__(self):
        return "Rubber Duck"

