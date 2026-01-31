from rule.Irule import IRule
from Iboard import IBoard

class RowRule(IRule):

    def __init__(self):
        super().__init__()

    def checkWin(self, sign: str, board: IBoard):
        size = board.getSize()
        for i in range(size):
            isSame = True
            for j in range(size):
                if board.getValue(i, j) != sign:
                    isSame = False
                    break
            if isSame == True:
                return True
        return False