from Structural.facade.auth_token import AuthToken
from Structural.facade.connection import Connection
from Structural.facade.message import Message


class NotificationServer:
    def connect(self, ip_address: str) -> Connection:
        return Connection(ip_address)

    def authenticate(self, app_id: str, key: str) -> AuthToken:
        print(f"App with id={app_id} and key={key} was authenticate")
        return AuthToken()

    def send(self, auth_token: AuthToken, message: Message, target: str):
        print(f" AuthToken={auth_token}")
        print(f"Sending a message {message} to {target}")
