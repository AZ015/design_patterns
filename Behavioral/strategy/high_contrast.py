from Behavioral.strategy.filter import Filter


class HighContrast(Filter):
    def apply(self) -> str:
        return "HIGH CONTRAST filter was apply"
