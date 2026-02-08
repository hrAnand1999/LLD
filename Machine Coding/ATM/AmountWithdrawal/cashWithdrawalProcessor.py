
from ATMRoomComponents.atm import ATM


class CashWithdrawalProcessor:

    def __init__(self, nextCashWithdrawalProcessor=None):
        self.nextCashWithdrawalProcessor = nextCashWithdrawalProcessor

    def processCashWithdrawal(self, amount, atm: ATM):
        if self.nextCashWithdrawalProcessor is not None:
            self.nextCashWithdrawalProcessor.processCashWithdrawal(amount, atm)



        