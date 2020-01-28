from Behavioral.observer.simple_observer.observer import Observer


class Chart(Observer):
    def update(self) -> None:
        print("Chart got notify")
