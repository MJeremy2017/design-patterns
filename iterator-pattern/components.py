class MenuComponent:
    def add(self, menu_component):
        raise NotImplementedError

    def remove(self, menu_component):
        raise NotImplementedError

    def get_child(self, index: int):
        raise NotImplementedError

    def get_name(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError

    def is_vegan(self):
        raise NotImplementedError

    def print_menu(self):
        raise NotImplementedError

    def get_menu_iterator(self):
        raise NotImplementedError
