from abc import ABC, abstractmethod


class Quackable(ABC):
    @abstractmethod
    def quack(self):
        ...
