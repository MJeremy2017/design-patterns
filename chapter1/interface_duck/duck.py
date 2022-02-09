from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def quack(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class RedheadDuck(Duck, Flyable):

    def swim(self):
        return "paddling"

    def quack(self):
        return "redhead quack"

    def fly(self):
        return "redhead fly"

    def display(self):
        return "redhead duck"


# now rubber duck does not need to fly
class RubberDuck(Duck):
    def display(self):
        return "rubber duck"

    def swim(self):
        return "floating"

    def quack(self):
        return "jioooo"


# TODO: more ducks fly in different ways


if __name__ == '__main__':
    rubber_duck = RubberDuck()
    redhead_duck = RedheadDuck()

