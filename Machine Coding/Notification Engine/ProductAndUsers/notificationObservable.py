from ProductAndUsers.observableInterface import ObservableInterface
from Notification.notificationInterface import NotificationInterface
from ProductAndUsers.observerInterface import ObserverInterface
from typing import List

class NotificationObservable(ObservableInterface):
    def __init__(self, name: str):
        self.observers: List[ObserverInterface] = [] 
        self.name = name

    def add(self, observer):
        self.observers.append(observer) 

    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            # print(observer.name)
            observer.update(message)

    def getNotification(self):
        return self.notification
    
    def setNotification(self, notification: NotificationInterface):
        self.notification = notification
        # print(notification.getContent())
        return self.notify(notification.getContent())
    
