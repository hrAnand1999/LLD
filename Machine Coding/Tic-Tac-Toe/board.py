from Iboard import IBoard

class Board(IBoard):

    def __init__(self, size: int):
        self.size = size
        self.bd = [["#" for _ in range(size)] for _ in range(size)]

    def getValue(self, row, col):
        return self.bd[row][col]
    
    def setValue(self, row, col, sign):
        self.bd[row][col] = sign

    def getSize(self):
        return self.size
    
    def isEmptyCell(self, row: int, col: int) -> bool:
        return self.bd[row][col] == '#'