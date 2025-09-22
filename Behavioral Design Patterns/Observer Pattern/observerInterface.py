from abc import ABC, abstractmethod

class ObserverInterface:

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def unsubsribe(self):
        pass