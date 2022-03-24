from typing import List


class MenuItem:
    def __init__(self, name: str, vegan: bool, price: float):
        self.name = name
        self.vegan = vegan
        self.price = price

    def __str__(self):
        return f"{self.name}     vegan: {self.vegan}       {self.price}$"


class DinerMenu:
    def __init__(self):
        self.menu: List[MenuItem] = []

    def add_item(self, name: str, vegan: bool, price: float):
        item = MenuItem(name, vegan, price)
        self.menu.append(item)

    def get_menu(self):
        return self.menu

