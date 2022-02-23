from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, size: int):
        self.description = ""
        self.size = size

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass

    def get_size(self) -> int:
        return self.size


class Espresso(Beverage):
    def __init__(self, size):
        super().__init__(size)
        self.description = "Espresso"

    def cost(self) -> float:
        return 2


class HouseBlend(Beverage):
    def __init__(self, size):
        super().__init__(size)
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.99


if __name__ == '__main__':
    esp = Espresso(1)
    print(esp.get_description())
    print(esp.get_size())
    print(esp.cost())
