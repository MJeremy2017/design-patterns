class GumballMachine:
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3

    def __init__(self, count):
        self.count = count
        self.state = GumballMachine.SOLD_OUT
        if count > 0:
            self.state = GumballMachine.NO_QUARTER

    def insert_quarter(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("You can’t insert another quarter")
        elif self.state == GumballMachine.NO_QUARTER:
            self.state = GumballMachine.HAS_QUARTER
            print("You inserted a quarter")
        elif self.state == GumballMachine.SOLD_OUT:
            print("You can’t insert a quarter, the machine is sold out")
        elif self.state == GumballMachine.SOLD:
            print("Please wait, we’re already giving you a gumball")

    def eject_quarter(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("Quarter returned")
            self.state = GumballMachine.NO_QUARTER
        elif self.state == GumballMachine.NO_QUARTER:
            print("You haven’t inserted a quarter")
        elif self.state == GumballMachine.SOLD:
            print("Sorry, you already turned the crank")
        elif self.state == GumballMachine.SOLD_OUT:
            print("You can’t eject, you haven’t inserted a quarter yet")

    def turn_crank(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("You turned...")
            self.state = GumballMachine.SOLD
            self.dispense()
        elif self.state == GumballMachine.NO_QUARTER:
            print("You turned but there’s no quarter")
        elif self.state == GumballMachine.SOLD:
            print("Turning twice doesn't get you another gumball!")
        elif self.state == GumballMachine.SOLD_OUT:
            print("You turned, but there are no gumballs")

    def dispense(self):
        if self.state == GumballMachine.SOLD:
            print("A gumball comes rolling out the slot")
            self.count -= 1
            if self.count == 0:
                print("Oops, out of gumballs!")
                self.state = GumballMachine.SOLD_OUT
            else:
                self.state = GumballMachine.NO_QUARTER
        elif self.state == GumballMachine.NO_QUARTER:
            print("You need to pay first")
        elif self.state == GumballMachine.SOLD_OUT:
            print("No gumball dispensed")
        elif self.state == GumballMachine.HAS_QUARTER:
            print("No gumball dispensed")

    def __str__(self):
        state_mapping = {
            0: "SOLD_OUT",
            1: "NO_QUARTER",
            2: "HAS_QUARTER",
            3: "SOLD",
        }
        return f"current state {state_mapping[self.state]} gumball left {self.count}"
