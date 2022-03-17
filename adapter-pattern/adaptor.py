from duck import *
from turkey import *


class TurkeyAdaptor(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


def test_duck(duck: Duck):
    duck.quack()
    duck.fly()


if __name__ == '__main__':
    mallard_duck = MallardDuck()
    wild_turkey = WildTurkey()

    turkey_adaptor = TurkeyAdaptor(wild_turkey)

    print("Mallard Duck ==========================")
    test_duck(mallard_duck)

    print("Adaptor Turkey ==========================")
    test_duck(turkey_adaptor)