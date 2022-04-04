from gumball_machine import GumballMachine

def main():
    gm = GumballMachine(5)
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


if __name__ == '__main__':
    main()