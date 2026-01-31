from abc import ABC, abstractmethod
from Iboard import IBoard

class IRule(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def checkWin(self, sign: str, board: IBoard) -> bool:
        pass

