from abc import ABC, abstractmethod


class GumballMachineRemote(ABC):
    """
    This is the proxy
    """
    @abstractmethod
    def get_count(self) -> int:
        pass

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_location(self) -> str:
        pass


class GumballMonitor:
    """
    This is the client which relies on the remote object(proxy) instead of gumball machine
    """

    def __init__(self, gumball_machine: GumballMachineRemote):
        self.gumball_machine = gumball_machine

    def report(self):
        print("location", self.gumball_machine.get_location())
        print("gumball count", self.gumball_machine.get_count())
        print("machine state", self.gumball_machine.get_state())
