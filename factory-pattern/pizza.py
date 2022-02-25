from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


class CheesePizza(Pizza):
    def prepare(self):
        print("preparing a cheese pizza")

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class ClamPizza(Pizza):
    def prepare(self):
        print("preparing a clam pizza")

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class TurkeyPizza(Pizza):
    def prepare(self):
        print("preparing a turkey pizza")

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class NYStyleCheesePizza(CheesePizza):
    def box(self):
        print("box a NY stype cheese pizza")


class NYStyleClamPizza(ClamPizza):
    def box(self):
        print("box a NY stype clam pizza")


class NYStyleTurkeyPizza(TurkeyPizza):
    def box(self):
        print("box a NY stype turkey pizza")
