class PaymentStrategy:

    def __init__(self, strategy):
        self.strategy = strategy

    def setStrategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)