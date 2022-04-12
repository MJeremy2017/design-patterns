from gumball_monitor import GumballMonitor, StateGumballMachine


gumball_machine = StateGumballMachine("The Tennery", 12)
monitor = GumballMonitor(gumball_machine)

monitor.report()


