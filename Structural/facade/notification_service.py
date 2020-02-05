from Structural.facade.message import Message
from Structural.facade.notification_server import NotificationServer


class NotificationService:
    def send(self, message: str, target: str):
        server = NotificationServer()
        connection = server.connect("ip")
        auth_token = server.authenticate("appId", "key")
        server.send(auth_token=auth_token, message=Message(message), target=target)
        connection.disconnect()
