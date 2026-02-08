from ATMStates.atmState import ATMState
from ATMRoomComponents.atm import ATM
from ATMRoomComponents.card import Card


class IdleState(ATMState):

    def __init__(self):
        super().__init__()

    
    def insertCard(self, card: Card, atm: ATM):
        print("Card inserted successfully")
        # local import to avoid circular dependency
        from ATMStates.hasCardState import HasCardState
        atm.setAtmState(HasCardState())
        