from paymentInterface import PaymentInterface

class UPI(PaymentInterface):

    def __init__(self):
        super().__init__()

    def pay(self, amount: str):
        print(f'Paying amount : {amount} via UPI')