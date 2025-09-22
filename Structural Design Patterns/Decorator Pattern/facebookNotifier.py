from notifierDecorator import NotifierDecorator

class Facebook(NotifierDecorator):

    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message):
        print(f'Notification Facebook class: {message}')
        self.notifier.notify(message)