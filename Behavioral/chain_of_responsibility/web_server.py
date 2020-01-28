from Behavioral.chain_of_responsibility import Handler, HttpRequest


class WebServer:
    def __init__(self, handler: Handler):
        self._handler = handler

    def handle(self, request: HttpRequest):
        self._handler.handle(request)
