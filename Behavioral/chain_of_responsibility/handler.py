from abc import ABC, abstractmethod

from Behavioral.chain_of_responsibility import HttpRequest


class Handler(ABC):
    def __init__(self, next_):
        self._next = next_

    def handle(self, request: HttpRequest) -> bool:
        if self.do_handle(request):
            return False
        if self._next is not None:
            self._next.handle(request)

    @abstractmethod
    def do_handle(self, http_request: HttpRequest) -> bool:
        pass
