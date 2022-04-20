from abc import ABC, abstractmethod
import observer


class Quackable(ABC):
    def __init__(self):
        # composition
        self.observable: observer.Observable = observer.Observable(self)

    @abstractmethod
    def quack(self):
        ...

    def register_observer(self, observer: observer.Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def __str__(self):
        raise NotImplementedError
