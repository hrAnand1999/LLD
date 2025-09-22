from Notification.notificationInterface import NotificationInterface

class SimpleNotification(NotificationInterface):
    
    def __init__(self, content):
        self.content = content

    def getContent(self):
        return self.content