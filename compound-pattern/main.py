from duck import *
from goose import Goose
from adapter import GooseAdapter
from decorator import QuackCounter


def simulate(duck: Quackable):
    duck.quack()


if __name__ == '__main__':
    mallard_duck = QuackCounter(MallardDuck())
    duck_call = QuackCounter(DuckCall())
    redhead_duck = QuackCounter(RedHeadDuck())
    rubber_duck = QuackCounter(RubberDuck())
    goose_adapter = QuackCounter(GooseAdapter(Goose()))

    simulate(mallard_duck)
    simulate(redhead_duck)
    simulate(duck_call)
    simulate(rubber_duck)
    simulate(goose_adapter)
    print("Total quack counter", QuackCounter.get_quack_count())
