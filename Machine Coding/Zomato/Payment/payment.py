from paymentInterface import PaymentInterface

class Payment(PaymentInterface):

    def __init__(self, strategy: PaymentInterface):
        self.strategy = strategy

    def pay(self, amount: int):
        self.strategy.pay(amount)