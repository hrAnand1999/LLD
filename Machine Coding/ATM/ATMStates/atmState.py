from abc import ABC, abstractmethod


class ATMState(ABC):

    def __init__(self):
        super().__init__()

    
    def insertCard(self):
        pass

   
    def authenticatePin(self):
        pass

   
    def returnCard(self):
        pass

    
    def exit(self):
        pass

   
    def selectOperation(self, operation, atm, card):
        pass

    
    def checkBalance(self):
        pass

    def cashWithdrawal(self):
        pass