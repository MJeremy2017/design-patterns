from gumball_machine import GumballMachine
from state_gumball_machine import StateGumballMachine


def main():
    gm = StateGumballMachine(5)
    print(gm)

    gm.insert_quarter()
    gm.turn_crank()
    print(gm)

    gm.insert_quarter()
    gm.eject_quarter()
    gm.turn_crank()
    print(gm)

    gm.insert_quarter()
    gm.turn_crank()
    gm.insert_quarter()
    gm.turn_crank()
    gm.eject_quarter()
    print(gm)

    gm.insert_quarter()
    gm.insert_quarter()
    gm.turn_crank()
    gm.insert_quarter()
    gm.turn_crank()
    gm.insert_quarter()
    gm.turn_crank()
    gm.refill(10)
    print(gm)


if __name__ == '__main__':
    main()
