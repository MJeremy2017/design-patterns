from abc import abstractmethod, ABC
from menu import *


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


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


if __name__ == '__main__':
    dm = DinerMenu()
    dm.add_item("gg", True, 12)
    dm.add_item("uu", False, 10)

    menu = dm.get_menu()

    dmi = DinerMenuIterator(menu)

    while dmi.has_next():
        item = dmi.next()
        print(item)
