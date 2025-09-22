from ProductAndUsers.observerInterface import ObserverInterface
from typing import List
from NotificationStrategy.notificationStrategyInterface import NotificationInterface


class Observer(ObserverInterface):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.notification_method : List[NotificationInterface] = []

    def update(self, message):
        # print(f"{self.name} received notification: {message}")
        for method in self.notification_method:
            # print(method.email_address if hasattr(method, 'email_address') else (method.phone_number if hasattr(method, 'phone_number') else 'Unknown'))
            method.send_notification(message)

    def setNotificationMethod(self, notification_method):
        self.notification_method.append(notification_method)

    def getNotificationMethod(self):
        return self.notification_method 
    
    def removeNotificationMethod(self, notification_method):
        self.notification_method.remove(notification_method)