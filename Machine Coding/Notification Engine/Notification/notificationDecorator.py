from Notification.notificationInterface import NotificationInterface
from abc import abstractmethod

class NotificationDecorator(NotificationInterface):

    def __init__(self):
        pass
    
    @abstractmethod
    def getContent(self):
        pass