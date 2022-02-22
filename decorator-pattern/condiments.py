from abc import abstractmethod
from beverage import Beverage


# condiments is a abstract class
class CondimentsDecorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Mocha(CondimentsDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "+ Mocha"

    def cost(self):
        # delegate cost calculation to beverage and add on the current cost
        return 0.2 + self.beverage.cost()


class Whip(CondimentsDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "+ Whip"

    def cost(self):
        return 0.5 + self.beverage.cost()

