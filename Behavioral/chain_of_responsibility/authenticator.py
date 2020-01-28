from Behavioral.chain_of_responsibility import Handler, HttpRequest


class Authenticator(Handler):
    def __init__(self, next_: Handler):
        super().__init__(next_)

    def authenticate(self, http_request: HttpRequest) -> bool:
        pass

    def do_handle(self, request: HttpRequest) -> bool:
        is_valid = request.username == "admin" \
                   and request.password == "1234"
        print("Authentication")
        return not is_valid
