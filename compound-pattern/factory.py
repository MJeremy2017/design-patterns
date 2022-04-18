from abc import ABC, abstractmethod
from duck import *
from decorator import QuackCounter


class AbstractDuckFactory(ABC):

    @abstractmethod
    def create_mallard_duck(self):
        ...

    @abstractmethod
    def create_redhead_duck(self):
        ...

    @abstractmethod
    def create_duck_call(self):
        ...

    @abstractmethod
    def create_rubber_duck(self):
        ...


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedHeadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedHeadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())
