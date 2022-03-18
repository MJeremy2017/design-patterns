from abc import ABC, abstractmethod


class Enumerator(ABC):
    """
    Old Adaptee Class
    """

    @abstractmethod
    def has_more_elements(self):
        pass

    @abstractmethod
    def next_element(self):
        pass


class Iterator(ABC):
    """
    New one, the Target Class
    """

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class EnumerationIterator(Iterator):
    """
    Adaptor: Type is Iterator
    Converts old Enumerator to Iterator class
    """

    def __init__(self, enum: Enumerator):
        self.enum: Enumerator = enum

    def has_next(self):
        return self.enum.has_more_elements()

    def next(self):
        return self.enum.next_element()

    def remove(self):
        return NotImplementedError("remove is not implemented")
