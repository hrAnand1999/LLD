from ATMRoomComponents.bankAccount import BankAccount
from ATMRoomComponents.card import Card

class User:

    def __init__(self, name, card, bankAccount):
        self.name = name
        self.card = card
        self.bankAccount = bankAccount

    def getName(self):
        return self.name
    
    def getCard(self):
        return self.card
    
    def getBankAccount(self):
        return self.bankAccount