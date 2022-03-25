from iterator import *


class Waitress:
    def __init__(self, diner_menu: Menu):
        self.diner_menu: Menu = diner_menu

    def present_menu(self):
        """
        It operates on a common interface Iterator, which prevent the client to deal with the implementation details
        of each type of Menu
        :return:
        """
        diner_menu_iter: Iterator = self.diner_menu.get_menu_iterator()
        while diner_menu_iter.has_next():
            print(diner_menu_iter.next())


if __name__ == '__main__':
    diner_menu = DinerMenu()
    diner_menu.add_item("Mushroom Sprinkle", True, 12.4)
    diner_menu.add_item("Meat Feast", False, 18)

    waitress = Waitress(diner_menu)
    waitress.present_menu()