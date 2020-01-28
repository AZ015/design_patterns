from Behavioral.observer.simple_observer.observer import Observer


class SpreadSheet(Observer):
    def update(self) -> None:
        print("Spreadsheet got notify")
