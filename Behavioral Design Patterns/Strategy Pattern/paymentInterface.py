from abc import abstractmethod

class PaymentInterface:

    def __init__(self):
        pass
    
    @abstractmethod
    def pay(self, amount: str):
        pass