from ATMStates.atmState import ATMState
from ATMRoomComponents.atm import ATM
from ATMRoomComponents.card import Card
from ATMStates.idleState import IdleState


class CheckBalanceState(ATMState):

    def __init__(self):
        print("Your current balance is: ")

    def checkBalance(self, atm: ATM, card: Card):
        print(card.getBalance())

    def exit(self, atm: ATM):
        self.returnCard()
        atm.setAtmState(IdleState())
        print("Exited successfully")

    def returnCard(self):
        print("Please collect your card")
        return