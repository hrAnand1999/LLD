from notifierInterface import NotifierInterface

class Notifier(NotifierInterface):

    def __init__(self):
        pass

    def notify(self, message:str):
        print(f'Notification Base class: {message}')