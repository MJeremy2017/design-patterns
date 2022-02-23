from beverage import *
from condiments import *


if __name__ == '__main__':
    size = 1
    beverage: Beverage = Espresso(size)
    beverage: Beverage = Mocha(beverage)
    beverage: Beverage = Whip(beverage)

    print(beverage.get_description())
    print(beverage.cost())
    