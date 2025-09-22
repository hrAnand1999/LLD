from paymentInterface import PaymentInterface

class NetBanking(PaymentInterface):

    def __init__(self):
        super().__init__()

    def pay(self, amount: str):
        print(f'Paying amount : {amount} via NetBanking')