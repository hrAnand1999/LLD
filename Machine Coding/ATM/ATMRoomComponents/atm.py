from ATMStates.atmState import ATMState

class ATM:

    def __init__(self, atmState: ATMState, balance, twoThousandNote, fiveHundredNote, hundredNote):
        self.atmState = atmState
        self.balance = balance
        self.twoThousandNote = twoThousandNote
        self.fiveHundredNote = fiveHundredNote
        self.hundredNote = hundredNote

    def setAtmState(self, atmState: ATMState):
        self.atmState = atmState    

    def getAtmState(self):
        return self.atmState
    
    def getBalance(self):
        return self.balance
    
    def setBalance(self, balance):
        self.balance = balance
    
    def getTwoThousandNote(self):
        return self.twoThousandNote
    
    def setTwoThousandNote(self, twoThousandNote):
        self.twoThousandNote = twoThousandNote

    def getFiveHundredNote(self):
        return self.fiveHundredNote
    
    def setFiveHundredNote(self, fiveHundredNote):
        self.fiveHundredNote = fiveHundredNote  
    
    def getHundredNote(self):
        return self.hundredNote 
    
    def setHundredNote(self, hundredNote):
        self.hundredNote = hundredNote

    