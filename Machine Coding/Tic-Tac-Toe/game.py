from Iboard import IBoard
from rule.Irule import IRule
from collections import deque
from notifier.Iobserver import IObserver

class Game:
    def __init__(self, board: IBoard, rules: list[IRule]):
        self.board = board
        self.isOver = False
        self.rules = rules
        self.users = deque()
        self.observers = []

    def addUser(self, user):
        self.users.append(user)

    def addObserver(self, observer: IObserver):
        self.observers.append(observer)

    def notify(self, msg: str):
        for obs in self.observers:
            obs.update(msg)

    def checkWin(self, sign: str)-> bool:
        for rule in self.rules:
            if rule.checkWin(sign, self.board) == True:
                return True
        return False
    
    def isValidPos(self, row: int, col: int) -> bool:
        size = self.board.getSize()
        if row >= 0 and row < size and col >= 0 and col < size and self.board.isEmptyCell(row, col):
            return True
        return False
    
    def takeInput(self) -> list:
        row = int(input("Enter row value: "))
        col = int(input("Enter col value: "))
        return [row, col]
    
    def isDrawn(self) -> bool:
        size = self.board.getSize()
        for i in range(size):
            for j in range(size):
                if self.board.isEmptyCell(i, j) == True:
                    return False
                
        return True
    
    def play(self):
        self.notify("Tic Tac Toe Game started")

        while not self.isOver:
            if self.isDrawn() == True:
                self.notify("Game draw")
                self.isOver = True
                break
            user = self.users.popleft()
            self.notify(f'userId: {user.getId()} userName: {user.getName()} Please put your position')
            inp = self.takeInput()
            isValidPosition = False
            while not isValidPosition:
                isValidPosition = self.isValidPos(inp[0], inp[1])
                if isValidPosition == False:
                    self.notify("Please enter valid position")
                    inp = self.takeInput()
            
            sign = user.getSign()
            self.board.setValue(inp[0], inp[1], sign)
            if self.checkWin(sign) == True:
                self.notify(f'userId: {user.getId()} userName: {user.getName()} has won')
                self.isOver = True
            
            self.users.append(user)
        


