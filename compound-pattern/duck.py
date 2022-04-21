from base import Quackable
from observer import Observer, Observable


class MallardDuck(Quackable):
    def __init__(self):
        self.observable: Observable = Observable()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.observable.notify_observers(duck)

    def quack(self):
        print("Quack")
        self.notify_observers(self)

    def __str__(self):
        return "Mallard Duck"


class RedHeadDuck(Quackable):
    def __init__(self):
        self.observable: Observable = Observable()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.observable.notify_observers(duck)

    def quack(self):
        self.notify_observers(self)
        print("Quack")

    def __str__(self):
        return "Redhead Duck"


class DuckCall(Quackable):
    def __init__(self):
        self.observable: Observable = Observable()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.observable.notify_observers(duck)

    def quack(self):
        self.notify_observers(self)
        print("Kwak")

    def __str__(self):
        return "Duck Call"


class RubberDuck(Quackable):
    def __init__(self):
        self.observable: Observable = Observable()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.observable.notify_observers(duck)

    def quack(self):
        self.notify_observers(self)
        print("Squeak")

    def __str__(self):
        return "Rubber Duck"

