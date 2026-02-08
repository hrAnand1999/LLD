from ATMStates.atmState import ATMState
from ATMRoomComponents.atm import ATM
from ATMRoomComponents.card import Card
from ATMStates.idleState import IdleState
from AmountWithdrawal.HundredWithdrawal import OneHundredWithdrawal
from AmountWithdrawal.TwoThousandWithdrawal import TwoThousandWithdrawal
from AmountWithdrawal.FiveHundredWithdrawal import FiveHundredWithdrawal
from AmountWithdrawal.cashWithdrawalProcessor import CashWithdrawalProcessor


class CashWithdrawalState(ATMState):

    def __init__(self):
        print("Please enter the amount you want to withdraw")

    def withdrawCash(self, amount, atm: ATM, card: Card):
        if card.getBalance() >= amount:
            print("Cash withdrawn successfully")
            # Initialize the chain of responsibility
            cashWithdrawalProcessor = CashWithdrawalProcessor(TwoThousandWithdrawal(FiveHundredWithdrawal(OneHundredWithdrawal(None))))
            cashWithdrawalProcessor.processCashWithdrawal(amount, atm)
        else:
            print("Insufficient balance")
            self.exit(atm)

    def exit(self, atm: ATM):
        self.returnCard()
        atm.setAtmState(IdleState())
        print("Exited successfully")

    def returnCard(self):
        print("Please collect your card")
        return