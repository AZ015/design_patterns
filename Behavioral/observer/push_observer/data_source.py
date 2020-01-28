from Behavioral.observer.push_observer import Subject


class DataSource(Subject):

    def __init__(self) -> None:
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: object):
        self._value = value
        self.notify_observers(value)
