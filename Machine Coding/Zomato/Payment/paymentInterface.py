from abc import ABC, abstractmethod

class PaymentInterface(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def pay(self, amount: int):
        pass
