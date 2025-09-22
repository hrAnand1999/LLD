from fileSystemInterface import FileSystemInterface

class Folder(FileSystemInterface):

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.nested = []

    def ls(self):
        print('Listing folder: ', self.name)
        for item in self.nested:
            print('name: ', item.getName(), ' size: ', item.getSize())

    def openAll(self):
        print('Opening folder: ', self.name)
        for item in self.nested:
            item.openAll()

    def getSize(self):
        total = 0
        for item in self.nested:
            total += item.getSize()
        return total
    
    def getName(self):
        return self.name
    
    def cd(self, target: str):
        for item in self.nested:
            if item.isFolder() and item.getName() == target:
                print('Changing directory to folder: ', item.getName())
                return
        print('Folder: ', target, ' not found in folder: ', self.name)

    def add(self, item: FileSystemInterface):
        self.nested.append(item)
        # print('Added item: ', item.getName(), ' to folder: ', self.name)
        # print('Folder: ', self.name, ' new size: ', self.size)

    def isFolder(self) -> bool:
        return True

    