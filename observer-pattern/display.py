from abc import abstractmethod, ABC


class Display(ABC):
    @abstractmethod
    def display(self):
        pass
