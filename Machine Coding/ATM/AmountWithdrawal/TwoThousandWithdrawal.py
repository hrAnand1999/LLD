from AmountWithdrawal.cashWithdrawalProcessor import CashWithdrawalProcessor
from ATMRoomComponents.atm import ATM

class TwoThousandWithdrawal(CashWithdrawalProcessor):

    def __init__(self, nextCashWithdrawalProcessor=None):
        self.nextCashWithdrawalProcessor = nextCashWithdrawalProcessor

    def processCashWithdrawal(self, amount, atm: ATM):
        if amount >= 2000:
            numOfTwoThousands = amount // 2000
            if atm.getTwoThousandNote() >= numOfTwoThousands:
                print(f"Dispensed {numOfTwoThousands} 2000 notes")
                atm.setTwoThousandNote(atm.getTwoThousandNote() - numOfTwoThousands)
                amount = amount % 2000
            else:
                print(f"Dispensed {atm.getTwoThousandNote()} 2000 notes")
                amount = amount - (atm.getTwoThousandNote() * 2000)
                atm.setTwoThousandNote(0)
        
        if self.nextCashWithdrawalProcessor is not None:
            self.nextCashWithdrawalProcessor.processCashWithdrawal(amount, atm)

        elif amount > 0:
            print(f"Unable to dispense remaining amount of {amount} due to insufficient notes in the ATM")