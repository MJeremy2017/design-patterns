from duck import *
from goose import Goose
from adapter import GooseAdapter
from decorator import QuackCounter
from factory import CountingDuckFactory, AbstractDuckFactory


def action(duck: Quackable):
    duck.quack()


def simulate(duck_factory: AbstractDuckFactory):
    mallard_duck = duck_factory.create_mallard_duck()
    duck_call = duck_factory.create_duck_call()
    redhead_duck = duck_factory.create_redhead_duck()
    rubber_duck = duck_factory.create_rubber_duck()
    goose_adapter = QuackCounter(GooseAdapter(Goose()))

    action(mallard_duck)
    action(duck_call)
    action(redhead_duck)
    action(rubber_duck)
    action(goose_adapter)
    print("Total quack counter", QuackCounter.get_quack_count())


if __name__ == '__main__':
    factory = CountingDuckFactory()
    simulate(factory)
