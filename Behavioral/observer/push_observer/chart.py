from Behavioral.observer.push_observer import Observer


class Chart(Observer):
    def update(self, value: object) -> None:
        print(f"Chart got notify {value}")
