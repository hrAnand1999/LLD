from abc import ABC, abstractmethod

class Report(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getDataInJSON(self):
        """
        Abstract method to get report data in JSON format.
        This method should be implemented by subclasses.
        """
        pass