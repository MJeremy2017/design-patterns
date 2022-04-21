from __future__ import annotations
from abc import abstractmethod
import observer


class Quackable(observer.QuackObservable):
    @abstractmethod
    def quack(self):
        ...

    def __str__(self):
        raise NotImplementedError
