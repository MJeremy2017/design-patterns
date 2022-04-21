from goose import Goose
from base import Quackable
from observer import Observable, Observer


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        self.goose = goose
        self.observable: Observable = Observable()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self, duck: Quackable):
        self.observable.notify_observers(duck)

    def quack(self):
        self.goose.honk()

    def __str__(self):
        return "goose"

