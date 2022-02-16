from abc import abstractmethod, ABC
from observer import Observer
from subject import Subject
from typing import List


class Display(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionDisplay(Display, Observer):
    def __init__(self, subject: Subject):
        self.subject = subject  # store the subject for future de-registration
        self.temp: float = 0.0
        self.humidity: float = 0.0
        self.subject.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        # update measures and display them
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"current conditions: temperature {self.temp} degree, humidity {self.humidity}")


class StatisticsDisplay(Display, Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.temp_list: List[float] = []
        self.subject.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temp_list.append(temp)
        self.display()

    def display(self):
        max_temp = max(self.temp_list)
        avg_temp = sum(self.temp_list)/len(self.temp_list)
        min_temp = min(self.temp_list)
        print(f"current statistics: max/avg/min temperature {max_temp}/{avg_temp}/{min_temp}")


class ForecastDisplay(Display, Observer):
    def __init__(self, subject: Subject):
        self.subject = subject
        self.current_temp: float = -1.0
        self.weather_status: int = 0
        self.subject.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.update_weather_status(temp)
        self.display()

    def display(self):
        if self.weather_status == 0:
            print(f"weather forecast is on the way")
        elif self.weather_status == 1:
            print(f"temperature is rising, sunny days ahead")
        else:
            print(f"temperature is going down, rainy days ahead")

    def update_weather_status(self, temp):
        if self.current_temp == -1:
            self.weather_status = 0
        if temp > self.current_temp:
            self.weather_status = 1
        else:
            self.weather_status = 2
        self.current_temp = temp
