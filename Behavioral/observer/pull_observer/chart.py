from Behavioral.observer.pull_observer.data_source import DataSource
from Behavioral.observer.pull_observer.observer import Observer


class Chart(Observer):

    def __init__(self, data_source: DataSource):
        self._data_source = data_source

    def update(self) -> None:
        print(f"Chart got notify {self._data_source.value}")
