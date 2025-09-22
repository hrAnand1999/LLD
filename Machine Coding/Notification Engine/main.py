from Notification.simpleNotification import SimpleNotification
from Notification.signatureDecorator import SignatureDecorator
from Notification.timestampDecorator import TimestampDecorator
from NotificationStrategy.notificationFactory import NotificationFactory 
from ProductAndUsers.notificationObservable import NotificationObservable
from ProductAndUsers.observer import Observer   
import time


if __name__ == "__main__":
    simpleNotification = SimpleNotification("This is a simple notification")
    signatureNotification = SignatureDecorator(simpleNotification, " - From Harsh Anand")
    timestampNotification = TimestampDecorator(signatureNotification, time.ctime())

    emailNotificationUser1 = NotificationFactory.get_notification_method("email", 'abc@gmail.com')
    smsNotificationUser1 = NotificationFactory.get_notification_method("sms", '98192')
    whatsAppNotificationUser2 = NotificationFactory.get_notification_method("whatsapp", '781881')

    notificationObservable = NotificationObservable("Product Launch")
    observer1 = Observer("User1")
    observer2 = Observer("User2")  
    observer1.setNotificationMethod(emailNotificationUser1)
    observer1.setNotificationMethod(smsNotificationUser1)
    observer2.setNotificationMethod(whatsAppNotificationUser2)

    notificationObservable.add(observer1)
    notificationObservable.add(observer2)
    # notificationObservable.setNotification(timestampNotification)

    notificationObservable.setNotification(signatureNotification)