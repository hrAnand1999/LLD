from ATMRoomComponents.bankAccount import BankAccount

class Card:

    def __init__(self, number, pin, expiryDate, cvv, bankAccount: BankAccount):
        self.number = number
        self.pin = pin
        self.expiryDate = expiryDate
        self.cvv = cvv
        self.bankAccount = bankAccount

    def getNumber(self):
        return self.number  
    
    def getPin(self):
        return self.pin
    
    def getExpiryDate(self):
        return self.expiryDate
    
    def getCvv(self):
        return self.cvv
    
    def getBankAccount(self):
        return self.bankAccount
    
    def getBalance(self):
        return self.bankAccount.getBalance()