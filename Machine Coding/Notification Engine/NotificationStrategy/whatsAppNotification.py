from NotificationStrategy.notificationStrategyInterface import NotificationInterface

class WhatsAppNotification(NotificationInterface):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send_notification(self, message: str) -> None:
        print(f"Sending WhatsApp message to {self.phone_number}: {message}")