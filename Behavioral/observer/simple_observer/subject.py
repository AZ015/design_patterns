from typing import List

from Behavioral.observer.simple_observer.observer import Observer


class Subject:

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remover_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        [observer.update() for observer in self._observers]
