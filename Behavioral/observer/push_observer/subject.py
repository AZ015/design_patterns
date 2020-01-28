from typing import List

from Behavioral.observer.push_observer import Observer


class Subject:

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remover_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, value) -> None:
        [observer.update(value) for observer in self._observers]
