from NotificationStrategy.notificationStrategyInterface import NotificationInterface

class SMSNotification(NotificationInterface):

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send_notification(self, message: str) -> None:
        print(f"Sending SMS to {self.phone_number}: {message}")