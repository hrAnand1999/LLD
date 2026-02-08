from AmountWithdrawal.cashWithdrawalProcessor import CashWithdrawalProcessor
from ATMRoomComponents.atm import ATM

class FiveHundredWithdrawal(CashWithdrawalProcessor):

    def __init__(self, nextCashWithdrawalProcessor=None):
        self.nextCashWithdrawalProcessor = nextCashWithdrawalProcessor

    def processCashWithdrawal(self, amount, atm: ATM):
        if amount >= 500:
            numOfFiveHundreds = amount // 500
            if atm.getFiveHundredNote() >= numOfFiveHundreds:
                print(f"Dispensed {numOfFiveHundreds} 500 notes")
                atm.setFiveHundredNote(atm.getFiveHundredNote() - numOfFiveHundreds)
                amount = amount % 500
            else:
                print(f"Dispensed {atm.getFiveHundredNote()} 500 notes")
                amount = amount - (atm.getFiveHundredNote() * 500)
                atm.setFiveHundredNote(0)
        
        if self.nextCashWithdrawalProcessor is not None:
            self.nextCashWithdrawalProcessor.processCashWithdrawal(amount, atm)
        
        elif amount > 0:
            print(f"Unable to dispense remaining amount of {amount} due to insufficient notes in the ATM")