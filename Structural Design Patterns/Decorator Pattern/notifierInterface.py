from abc import abstractmethod

class NotifierInterface:

    def __init__(self):
        pass

    @abstractmethod
    def notify(self, message: str):
        pass