from abc import ABC, abstractmethod

class NotificationInterface(ABC):

    def __init__(self):
        pass    

    @abstractmethod
    def getContent(self):
        pass