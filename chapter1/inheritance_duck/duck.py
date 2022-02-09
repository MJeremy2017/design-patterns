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

    @abstractmethod
    def fly(self):
        pass


class RedheadDuck(Duck):

    def swim(self):
        return "paddling"

    def quack(self):
        return "redhead quack"

    def fly(self):
        return "redhead fly"

    def display(self):
        return "redhead duck"


# Here rubber duck shouldn't have fly functionality in the first place
class RubberDuck(Duck):
    def display(self):
        return "rubber duck"

    def swim(self):
        return "floating"

    def quack(self):
        return "jioooo"

    def fly(self):
        return "can't fly"


def let_the_duck_fly(duck: Duck) -> None:
    print(f"{duck.display()} flies like {duck.fly()}")


if __name__ == '__main__':
    rubber_duck = RubberDuck()
    redhead_duck = RedheadDuck()

    let_the_duck_fly(redhead_duck)
    # confusing to have a fly method
    let_the_duck_fly(rubber_duck)
