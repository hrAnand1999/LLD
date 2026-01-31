from rule.Irule import IRule
from Iboard import IBoard

class DiagRule(IRule):

    def __init__(self):
        super().__init__()

    def checkWin(self, sign: str, board: IBoard):
        size = board.getSize()
        i = 0
        j = 0
        isSame = True
        while i < size and j < size:
            if board.getValue(i, j) != sign:
                isSame = False
                break
            i += 1
            j += 1
        
        if isSame == True:
            return True
        
        i = 0
        j = size - 1
        while i < size and j >= 0:
            if board.getValue(i, j) != sign:
                isSame = False
                break
            i += 1
            j -= 1

        if isSame == True:
            return True
        
        return False