from beverage import *
from condiments import *


if __name__ == '__main__':
    beverage: Beverage = Espresso()
    beverage: Beverage = Mocha(beverage)
    beverage: Beverage = Whip(beverage)

    print(beverage.get_description())
    print(beverage.cost())
    