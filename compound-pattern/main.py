from duck import *
from goose import Goose
from adapter import GooseAdapter
from decorator import QuackCounter
from factory import CountingDuckFactory, AbstractDuckFactory
from composite import Flock
from observer import Quackologist


def action(duck: Quackable):
    duck.quack()


def simulate(duck_factory: AbstractDuckFactory):
    mallard_duck: MallardDuck = duck_factory.create_mallard_duck()
    duck_call: DuckCall = duck_factory.create_duck_call()
    redhead_duck = duck_factory.create_redhead_duck()
    rubber_duck = duck_factory.create_rubber_duck()
    goose_adapter = QuackCounter(GooseAdapter(Goose()))

    quakologist: Quackologist = Quackologist()
    mallard_duck.register_observer(quakologist)
    mallard_duck.quack()

    duck_call.register_observer(quakologist)
    duck_call.quack()

    # flock_ducks: Flock = Flock()
    # flock_ducks.add_duck(mallard_duck)
    # flock_ducks.add_duck(duck_call)
    # flock_ducks.add_duck(redhead_duck)
    # flock_ducks.add_duck(rubber_duck)
    # flock_ducks.add_duck(goose_adapter)
    #
    # action(flock_ducks)
    # print("Total quack counter", QuackCounter.get_quack_count())


if __name__ == '__main__':
    factory = CountingDuckFactory()
    simulate(factory)
