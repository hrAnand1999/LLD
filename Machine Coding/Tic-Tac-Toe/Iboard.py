from abc import ABC, abstractmethod

class IBoard(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def getValue(self, row: int, col: int) -> int:
        pass

    @abstractmethod
    def setValue(self, row: int, col: int, sign: str):
        pass

    @abstractmethod
    def getSize(self) -> int:
        pass

    @abstractmethod
    def isEmptyCell(self, row: int, col: int) -> bool:
        pass