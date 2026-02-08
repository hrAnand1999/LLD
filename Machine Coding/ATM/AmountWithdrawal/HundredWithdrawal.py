from AmountWithdrawal.cashWithdrawalProcessor import CashWithdrawalProcessor
from ATMRoomComponents.atm import ATM


class OneHundredWithdrawal(CashWithdrawalProcessor):

    def __init__(self, nextCashWithdrawalProcessor=None):
        self.nextCashWithdrawalProcessor = nextCashWithdrawalProcessor

    def processCashWithdrawal(self, amount, atm: ATM):
        if amount >= 100:
            numOfHundreds = amount // 100
            if atm.getHundredNote() >= numOfHundreds:
                print(f"Dispensed {numOfHundreds} 100 notes")
                atm.setHundredNote(atm.getHundredNote() - numOfHundreds)
                amount = amount % 100
            else:
                print(f"Dispensed {atm.getHundredNote()} 100 notes")
                amount = amount - (atm.getHundredNote() * 100)
                atm.setHundredNote(0)
        
        if self.nextCashWithdrawalProcessor is not None:
            self.nextCashWithdrawalProcessor.processCashWithdrawal(amount, atm)

        elif amount > 0:
            print(f"Unable to dispense remaining amount of {amount} due to insufficient notes in the ATM")