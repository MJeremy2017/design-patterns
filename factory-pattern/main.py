# TODO: what's good about the pattern
from pizza import *
from abc import ABC, abstractmethod


class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        """
        This acts as the pizza factory
        :param item: pizza type
        :return:
        """
        pass

    def order_pizza(self, item: str) -> Pizza:
        # the subclass handles the concrete pizza instantiation
        pizza: Pizza = self.create_pizza(item)
        pizza.prepare()
        pizza.cut()
        pizza.bake()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):

    def create_pizza(self, item: str) -> Pizza:
        if item == "cheese":
            return NYStyleCheesePizza()
        elif item == "clam":
            return NYStyleClamPizza()
        else:
            return NYStyleTurkeyPizza()


if __name__ == '__main__':
    store = NYPizzaStore()
    store.order_pizza("cheese")


