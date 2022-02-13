"""
Duck will now delegate its flying behavior,
instead of using flying methods defined in the Duck class (or subclass).
"""

from abc import ABC, abstractmethod


class Flyable(ABC):
    # say there is a bunch of other redundant functions ...
    @abstractmethod
    def fly(self):
        pass


class Duck(ABC):
    def __init__(self):
        self.flyable: Flyable = None

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def quack(self):
        pass

    def performFly(self):
        return self.flyable.fly()

    def setFlyBehaviour(self, fly_behaviour: Flyable):
        self.flyable = fly_behaviour


class FlyWithWings(Flyable):
    def fly(self):
        return "fly with wings"


class FlyWithRockets(Flyable):
    def fly(self):
        return "fly with rockets"


class RedheadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyable = FlyWithWings()

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def display(self):
        return "redhead duck"


# now objects can REUSE the fly method
class BlueheadDuck(Duck):
    def __init__(self):
        super(BlueheadDuck, self).__init__()
        self.flyable = FlyWithRockets()

    def swim(self):
        return "paddling"

    def quack(self):
        return "basic quack"

    def display(self):
        return "blue head duck"


if __name__ == '__main__':
    redhead_duck = RedheadDuck()
    bluehead_duck = BlueheadDuck()

    print(redhead_duck.performFly())
    print(bluehead_duck.performFly())

