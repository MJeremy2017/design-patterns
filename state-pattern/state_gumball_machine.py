class StateGumballMachine:
    def __init__(self, num_gumballs):
        self.count = num_gumballs
        self.no_quarter_state = NoQuarterState(self)
        self.sold_out_state = SoldOutState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        if num_gumballs > 0:
            self.state: State = self.no_quarter_state
        else:
            self.state: State = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        # gumball machine should not have a dispense method, it's defined internal in the turn_crank
        self.state.dispense()

    def set_state(self, state):
        self.state = state


class State:
    def insert_quarter(self):
        # this makes the method abstract
        raise NotImplementedError

    def eject_quarter(self):
        raise NotImplementedError

    def turn_crank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError


class NoQuarterState(State):
    def __init__(self, gumball_machine: StateGumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print("You haven’t inserted a quarter")

    def turn_crank(self):
        print("You turned but there’s no quarter")

    def dispense(self):
        print("You need to pay first")


class SoldOutState(State):
    def __init__(self, gumball_machine: StateGumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can’t insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You can’t eject, you haven’t inserted a quarter yet")

    def turn_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")


class HasQuarterState(State):
    def __init__(self, gumball_machine: StateGumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can’t insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def dispense(self):
        # inappropriate method for the state
        print("No gumball dispensed")


class SoldState(State):
    def __init__(self, gumball_machine: StateGumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we’re already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        print("A gumball comes rolling out the slot")
        self.gumball_machine.count -= 1
        if self.gumball_machine.count == 0:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)
        else:
            self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
