from Behavioral.chain_of_responsibility import Handler, HttpRequest


class Logger(Handler):
    def __init__(self, next_: Handler):
        super().__init__(next_)

    def do_handle(self, request: HttpRequest) -> bool:
        print("Log")
        return False
