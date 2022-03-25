from abc import abstractmethod, ABC
from typing import List


class MenuItem:
    def __init__(self, name: str, vegan: bool, price: float):
        self.name = name
        self.vegan = vegan
        self.price = price

    def __str__(self):
        return f"{self.name}     vegan: {self.vegan}       {self.price}$"


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Menu(ABC):
    @abstractmethod
    def get_menu_iterator(self) -> Iterator:
        pass


class DinerMenu(Menu):
    def __init__(self):
        self.menu: List[MenuItem] = []

    def add_item(self, name: str, vegan: bool, price: float):
        item = MenuItem(name, vegan, price)
        self.menu.append(item)

    def get_menu_iterator(self) -> Iterator:
        return DinerMenuIterator(self.menu)


class DinerMenuIterator(Iterator):
    def __init__(self, menu: List[MenuItem]):
        self.menu = menu
        self.__position = 0

    def has_next(self) -> bool:
        if self.__position < len(self.menu):
            return True
        return False

    def next(self) -> object:
        value: MenuItem = self.menu[self.__position]
        self.__position += 1
        return value
