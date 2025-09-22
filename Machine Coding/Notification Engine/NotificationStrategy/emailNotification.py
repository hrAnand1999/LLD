from NotificationStrategy.notificationStrategyInterface import NotificationInterface

class EmailNotification(NotificationInterface):

    def __init__(self, email_address: str):
        self.email_address = email_address

    def send_notification(self, message: str) -> None:
        print(f"Sending Email to {self.email_address}: {message}")
        