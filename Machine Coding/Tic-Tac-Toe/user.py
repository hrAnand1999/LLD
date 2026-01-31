class User:

    def __init__(self, id: int, name: str, sign: str):
        self.id = id
        self.name = name
        self.sign = sign

    def getId(self)-> int:
        return self.id
    
    def getName(self) -> str:
        return self.name
    
    def getSign(self) -> str:
        return self.sign
    
    