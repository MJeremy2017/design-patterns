from pizza import *


class SimplePizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "clam":
            return ClamPizza()
        else:
            return TurkeyPizza()

