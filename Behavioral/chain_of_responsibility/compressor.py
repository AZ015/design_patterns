from Behavioral.chain_of_responsibility import Handler, HttpRequest


class Compressor(Handler):
    def __init__(self, next_: Handler):
        super().__init__(next_)

    def do_handle(self, http_request: HttpRequest) -> bool:
        print("Compress")
        return False
