from abc import ABC, abstractmethod
from Notification.notificationInterface import NotificationInterface

class ObservableInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self, message):
        pass    

    @abstractmethod
    def getNotification(self):
        pass

    @abstractmethod
    def setNotification(self, notification: NotificationInterface):
        pass
