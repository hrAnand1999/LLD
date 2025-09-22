from notifierDecorator import NotifierDecorator

class SMS(NotifierDecorator):

    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message):
        print(f'Notification SMS class: {message}')
        self.notifier.notify(message)