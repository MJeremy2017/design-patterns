from abc import abstractmethod, ABC
from observer import Observer
from typing import List


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observer_list: List[Observer] = []
        self.temp: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def register_observer(self, observer: Observer):
        self.observer_list.append(observer)

    def remove_observer(self, observer: Observer):
        ind = self.observer_list.index(observer)
        self.observer_list.pop(ind)

    def notify_observer(self):
        for obs in self.observer_list:
            obs.update(self.temp, self.humidity, self.pressure)

    def set_measurements(self, temp: float, humidity: float, pressure: float):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observer()