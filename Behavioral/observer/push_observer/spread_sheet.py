from Behavioral.observer.push_observer import Observer


class SpreadSheet(Observer):
    def update(self, value: object) -> None:
        print(f"Spreadsheet got notify {value}")
