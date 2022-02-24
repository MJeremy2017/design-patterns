from pizza import Pizza
from factory import SimplePizzaFactory


class PizzaShop:
    def __init__(self, factory: SimplePizzaFactory):
        self.factory: SimplePizzaFactory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza = self.factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.cut()
        pizza.bake()
        pizza.box()

        return pizza


if __name__ == '__main__':
    pizza_factory = SimplePizzaFactory()
    pizza_shop = PizzaShop(pizza_factory)
    pizza: Pizza = pizza_shop.order_pizza("cheese")

