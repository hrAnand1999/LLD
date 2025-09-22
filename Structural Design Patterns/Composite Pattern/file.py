from fileSystemInterface import FileSystemInterface

class File(FileSystemInterface):

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def ls(self):
        print('name: ', self.name, ' size: ', self.size)

    def openAll(self):
        print('Opening file: ', self.name)

    def getSize(self):
        return self.size
    
    def getName(self):
        return self.name
    
    def cd(self):
        print('Cannot cd into a file: ', self.name)
        return None
    
    def isFolder(self)-> bool:
        return False