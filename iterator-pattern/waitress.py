from iterator import *


class Waitress:
    def __init__(self, menus: List[Menu]):
        self.menus = menus

    def present_menu(self, iterator: Iterator):
        """
        It operates on a common interface Iterator, which prevent the client to deal with the implementation details
        of each type of Menu
        :return:
        """
        # diner_menu_iter: Iterator = self.diner_menu.get_menu_iterator()
        while iterator.has_next():
            print(iterator.next())

    def run(self):
        for menu in self.menus:
            self.present_menu(menu.get_menu_iterator())


if __name__ == '__main__':
    diner_menu = DinerMenu()
    diner_menu.add_item("Mushroom Sprinkle", True, 12.4)
    diner_menu.add_item("Meat Feast", False, 18)

    cafe_menu = CafeMenu()
    cafe_menu.add_item("Latte", False, 6.9)
    cafe_menu.add_item("Cold Brew", False, 5.2)

    waitress = Waitress([diner_menu, cafe_menu])
    waitress.run()