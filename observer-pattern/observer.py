from abc import abstractmethod, ABC


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass





