from abc import ABC, abstractmethod

class AddressInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getPincode():
        pass