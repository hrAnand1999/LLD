from ATMStates.atmState import ATMState
from ATMRoomComponents.atm import ATM
from ATMRoomComponents.card import Card
from ATMStates.idleState import IdleState
from ATMStates.cashWithdrawalState import CashWithdrawalState
from ATMStates.checkBalanceState import CheckBalanceState


class SelectOperationState(ATMState):
    
    def __init__(self):
        print("Please select your operation")
        print("1. withdraw")
        print("2. check balance")


    def selectOperation(self, operation, atm: ATM, card: Card):
        if operation == "withdraw":
            atm.setAtmState(CashWithdrawalState())
            print("Withdraw selected")
        elif operation == "check balance":
            atm.setAtmState(CheckBalanceState())
            print("Check balance selected")
        else:
            print("Invalid operation selected")
            self.exit(atm)

    def exit(self, atm: ATM):
        self.returnCard()
        atm.setAtmState(IdleState())
        print("Exited successfully")

    def returnCard(self):
        print("Please collect your card")
        return