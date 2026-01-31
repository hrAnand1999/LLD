from rule.Irule import IRule
from Iboard import IBoard

class ColRule(IRule):

    def __init__(self):
        super().__init__()

    def checkWin(self, sign: str, board: IBoard):
        size = board.getSize()
        for j in range(size):
            isSame = True
            for i in range(size):
                if board.getValue(i, j) != sign:
                    isSame = False
                    break
            if isSame == True:
                return True
        return False