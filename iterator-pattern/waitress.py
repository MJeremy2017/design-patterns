from iterator import *


class Waitress:
    def __init__(self, menu: Menu):
        self.menu = menu

    def present_menu(self):
        """
        It operates on a common interface Iterator, which prevent the client to deal with the implementation details
        of each type of Menu
        :return:
        """
        # diner_menu_iter: Iterator = self.diner_menu.get_menu_iterator()
        self.menu.print_menu()

    # def run(self):
    #     for menu in self.menus:
    #         self.present_menu(menu.get_menu_iterator())


if __name__ == '__main__':
    dinner_menu = Menu('Dinner Menu')
    dinner_menu.add(MenuItem("Mushroom Sprinkle", True, 12.4))
    dinner_menu.add(MenuItem("Meat Feast", False, 18))
    cafe_menu = Menu('Cafe Menu')

    all_menus = Menu('All Menus')
    all_menus.add(dinner_menu)
    all_menus.add(cafe_menu)
    cafe_menu.add(MenuItem("Latte", False, 6.9))
    cafe_menu.add(MenuItem("Cold Brew", False, 5.2))

    waitress = Waitress(all_menus)
    waitress.present_menu()

    # diner_menu = DinerMenu()
    # diner_menu.add_item("Mushroom Sprinkle", True, 12.4)
    # diner_menu.add_item("Meat Feast", False, 18)
    #
    # cafe_menu = CafeMenu()
    # cafe_menu.add_item("Latte", False, 6.9)
    # cafe_menu.add_item("Cold Brew", False, 5.2)
    #
    # waitress = Waitress([diner_menu, cafe_menu])
    # waitress.run()