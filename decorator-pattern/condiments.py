from abc import abstractmethod
from beverage import Beverage


# condiments is a abstract class
class CondimentsDecorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Mocha(CondimentsDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage.get_size())
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "+ Mocha"

    def cost(self):
        # delegate cost calculation to beverage and add on the current cost
        if self.beverage.get_size() == 0:
            base_cost = 0.2
        else:
            base_cost = 0.5
        return base_cost + self.beverage.cost()


class Whip(CondimentsDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage.get_size())
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + "+ Whip"

    def cost(self):
        if self.beverage.get_size() == 0:
            base_cost = 0.5
        else:
            base_cost = 0.7
        return base_cost + self.beverage.cost()

