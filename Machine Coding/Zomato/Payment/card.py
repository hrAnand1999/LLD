from paymentInterface import PaymentInterface

class Card(PaymentInterface):
    
    def __init__(self):
        super().__init__()

    def pay(self, amount: int):
        print(f'Amount {amount} has been paid using Card method')