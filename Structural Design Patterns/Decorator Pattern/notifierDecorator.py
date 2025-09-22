from abc import abstractmethod
from notifierInterface import NotifierInterface

class NotifierDecorator(NotifierInterface):

    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.notify(message)

