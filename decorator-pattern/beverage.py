from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self.description = ""

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.99



if __name__ == '__main__':
    esp = Espresso()
    print(esp.get_description())