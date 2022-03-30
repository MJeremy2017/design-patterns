from abc import abstractmethod, ABC
from typing import List
from components import MenuComponent


class MenuItem(MenuComponent, ABC):
    def __init__(self, name: str, vegan: bool, price: float):
        self.name = name
        self.vegan = vegan
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def is_vegan(self):
        return self.vegan

    def print_menu(self):
        print(f"{self.name}     vegan: {self.vegan}       {self.price}$")


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Menu(MenuComponent, ABC):
    def __init__(self, name):
        self.name = name
        self.menu_components: List[MenuComponent] = []

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, index: int):
        return self.menu_components[index]

    def get_name(self):
        return self.name

    def print_menu(self):
        print(self.name)
        it = self.get_menu_iterator()
        while it.has_next():
            v: MenuComponent = it.next()
            v.print_menu()

    def get_menu_iterator(self) -> Iterator:
        return MenuIterator(self.menu_components)


class MenuIterator(Iterator):
    def __init__(self, menu):
        self.menu = menu
        self.__position = 0

    def has_next(self) -> bool:
        if self.__position >= len(self.menu):
            return False
        return True

    def next(self) -> object:
        v = self.menu[self.__position]
        self.__position += 1
        return v

# class DinerMenu(Menu):
#     def __init__(self):
#         self.menu: List[MenuItem] = []
#
#     def add_item(self, name: str, vegan: bool, price: float):
#         item = MenuItem(name, vegan, price)
#         self.menu.append(item)
#
#     def get_menu_iterator(self) -> Iterator:
#         return DinerMenuIterator(self.menu)
#
#
# class CafeMenu(Menu):
#     def __init__(self):
#         self.menu = dict()
#
#     def add_item(self, name: str, vegan: bool, price: float):
#         item = MenuItem(name, vegan, price)
#         self.menu[name] = item
#
#     def get_menu_iterator(self) -> Iterator:
#         return CafeMenuIterator(self.menu)
#
#
# class DinerMenuIterator(Iterator):
#     def __init__(self, menu: List[MenuItem]):
#         self.menu = menu
#         self.__position = 0
#
#     def has_next(self) -> bool:
#         if self.__position < len(self.menu):
#             return True
#         return False
#
#     def next(self) -> object:
#         value: MenuItem = self.menu[self.__position]
#         self.__position += 1
#         return value
#
#
# class CafeMenuIterator(Iterator):
#     def __init__(self, menu: dict):
#         self.menu = menu
#         self.keys = list(menu.keys())
#         self.__position = 0
#
#     def has_next(self) -> bool:
#         if self.__position >= len(self.keys):
#             return False
#         return True
#
#     def next(self) -> object:
#         value = self.menu[self.keys[self.__position]]
#         self.__position += 1
#         return value
