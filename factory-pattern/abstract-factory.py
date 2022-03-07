"""
Demonstration of abstract factory method against the general factory method
"""

from abc import ABC, abstractmethod


# should be an interface
class Dough:
    def __init__(self, name: str):
        self.name = name


# should be an interface
class Sauce:
    def __init__(self, name: str):
        self.name = name


class Clam:
    def __init__(self, name: str):
        self.name = name


class IngredientFactory:
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_clam(self) -> Clam:
        pass


class Pizza(ABC):
    def __init__(self, ingredients_factory: IngredientFactory):
        self.ingredients_factory = ingredients_factory

    @abstractmethod
    def prepare(self):
        pass


class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        pass

    def cook_pizza(self, pizza: Pizza):
        pizza.prepare()


class NYIngredientFactory(IngredientFactory):
    def create_clam(self) -> Clam:
        return Clam("Frozen Clam")

    def create_dough(self) -> Dough:
        return Dough("Thick Dough")

    def create_sauce(self) -> Sauce:
        return Sauce("Sour Sauce")


class CheesePizza(Pizza):
    def __init__(self, ingredients_factory: IngredientFactory):
        super().__init__(ingredients_factory)

    def prepare(self):
        self.ingredients_factory.create_dough()
        self.ingredients_factory.create_sauce()


class ClamPizza(Pizza):
    def __init__(self, ingredients_factory: IngredientFactory):
        super().__init__(ingredients_factory)

    def prepare(self):
        self.ingredients_factory.create_dough()
        self.ingredients_factory.create_sauce()
        # this makes the difference
        self.ingredients_factory.create_clam()


class NYPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredients_factory: IngredientFactory = NYIngredientFactory()

    def create_pizza(self, item: str) -> Pizza:
        if item == "cheese":
            pizza = CheesePizza(self.ingredients_factory)
        else:
            pizza = ClamPizza(self.ingredients_factory)
        return pizza
