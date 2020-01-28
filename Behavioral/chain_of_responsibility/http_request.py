class HttpRequest:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
