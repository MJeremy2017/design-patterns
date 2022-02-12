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
        return "basic quack"

    def fly(self):
        return "fly with wings"

    def display(self):
        return "redhead duck"


# now blue head duck flies the same as red head,
# and there is many other ducks need to copy and past the same fly method
class BlueheadDuck(Duck, Flyable):

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def fly(self):
        return "fly with wings"

    def display(self):
        return "blue head duck"


# now rubber duck does not need to fly
class RubberDuck(Duck):
    def display(self):
        return "rubber duck"

    def swim(self):
        return "floating"

    def quack(self):
        return "jioooo"


if __name__ == '__main__':
    rubber_duck = RubberDuck()
    redhead_duck = RedheadDuck()

