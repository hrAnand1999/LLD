from ATMStates.atmState import ATMState
from ATMRoomComponents.atm import ATM
from ATMRoomComponents.card import Card


class HasCardState(ATMState):

    def __init__(self):
        print("Please insert your card pin")
        super().__init__()

    def authenticatePin(self, pin, atm: ATM, card: Card):
        if card.getPin() == pin:
            print("Pin authenticated successfully")
            # move to select operation state
            from ATMStates.selectOperationState import SelectOperationState
            atm.setAtmState(SelectOperationState())
        else:
            print("Pin authentication failed")
            self.exit(atm)
        
    def exit(self, atm: ATM):
        self.returnCard()
        # local import to avoid circular dependency
        from ATMStates.idleState import IdleState
        atm.setAtmState(IdleState())
        print("Exited successfully")
    
    def returnCard(self):
        print("Please collect your card")
        return
        