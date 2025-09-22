from notifierDecorator import NotifierDecorator

class Slack(NotifierDecorator):

    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message:str):
        print(f'Notification Slack class: {message}')
        self.notifier.notify(message)