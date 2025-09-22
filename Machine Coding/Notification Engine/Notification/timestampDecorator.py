from Notification.notificationDecorator import NotificationDecorator


class TimestampDecorator(NotificationDecorator):

    def __init__(self, notification, timestamp):
        self.notification = notification
        self.timestamp = timestamp
    
    def getContent(self):
        return f"{self.notification.getContent()}\n\n{self.timestamp}"