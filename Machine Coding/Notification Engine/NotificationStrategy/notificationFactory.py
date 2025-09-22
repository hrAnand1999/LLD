from NotificationStrategy.emailNotification import EmailNotification
from NotificationStrategy.smsNotification import SMSNotification
from NotificationStrategy.whatsAppNotification import WhatsAppNotification


class NotificationFactory:
    @staticmethod
    def get_notification_method(method: str, contact: str):
        if method == "email":
            return EmailNotification(contact)
        elif method == "sms":
            return SMSNotification(contact)
        elif method == "whatsapp":
            return WhatsAppNotification(contact)
        else:
            raise ValueError(f"Unknown notification method: {method}")  