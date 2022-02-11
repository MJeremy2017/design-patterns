"""
Subclass of duck can inherit different fly behaviours
"""
from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Duck(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def quack(self):
        pass


class FlyWithWings(Flyable):
    def fly(self):
        return "fly with wings"


class FlyWithRockets(Flyable):
    def fly(self):
        return "fly with rockets"


class RedheadDuck(Duck, FlyWithWings):

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def display(self):
        return "redhead duck"


# now objects can REUSE the fly method
class BlueheadDuck(Duck, FlyWithRockets):

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def display(self):
        return "blue head duck"


if __name__ == '__main__':
    redhead_duck = RedheadDuck()
    bluehead_duck = BlueheadDuck()

    print(redhead_duck.fly())
    print(bluehead_duck.fly())

