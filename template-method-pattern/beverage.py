from abc import abstractmethod, ABC


class CaffeineBeverage(ABC):
    """
    Prepare is the template method
    - Some methods are handled by this class.
    - And some are handled by the subclass.
    """
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("boiling water")

    def pour_in_cup(self):
        print("pouring in cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


class Coffee(CaffeineBeverage):
    def brew(self):
        print("brewing coffee")

    def add_condiments(self):
        print("adding sugar and milk")


class Tea(CaffeineBeverage):
    def brew(self):
        print("steeping tea bag")

    def add_condiments(self):
        print("adding lemon")


if __name__ == '__main__':
    tea = Tea()
    tea.prepare()
