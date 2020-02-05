from Structural.facade.notification_service import NotificationService

if __name__ == '__main__':
    service = NotificationService()
    service.send("Hello World", "target")
