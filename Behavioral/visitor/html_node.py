from abc import ABC, abstractmethod

from Behavioral.visitor.operation import Operation


class HtmlNode(ABC):
    @abstractmethod
    def execute(self, operation: Operation):
        pass
