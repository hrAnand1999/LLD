from abc import ABC, abstractmethod

class ObservableInterface:

    def __init__(self):
        pass

    @abstractmethod
    def addObserver(self):
        pass

    @abstractmethod
    def removeObserver(self):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setData(self):
        pass

    @abstractmethod
    def getData(self):
        pass