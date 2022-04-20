from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import base


class Observer(ABC):
    @abstractmethod
    def update(self, duck: base.Quackable):
        ...


class QuackObservable(ABC):

    @abstractmethod
    def register_observer(self, observer: Observer):
        ...

    @abstractmethod
    def notify_observers(self):
        ...


class Observable(QuackObservable):
    def __init__(self, duck: base.Quackable):
        self.duck: base.Quackable = duck
        self.observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        print("observable registered")
        self.observers.append(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update(self.duck)


class Quackologist(Observer):
    def update(self, duck: base.Quackable):
        print("Quackologist", duck, "just quacked!")
