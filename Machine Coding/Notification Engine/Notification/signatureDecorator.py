from Notification.notificationDecorator import NotificationDecorator


class SignatureDecorator(NotificationDecorator):
    
    def __init__(self, notification, signature):
        self.notification = notification
        self.signature = signature
    
    def getContent(self):
        return f"{self.notification.getContent()}\n\n{self.signature}"