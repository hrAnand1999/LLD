from fileSystemInterface import FileSystemInterface
from folder import Folder
from file import File

class Client:
    def __init__(self):
        pass


    def createFolder(self, name: str, size: int)->FileSystemInterface:
        folder = Folder(name, size)
        return folder

    def createFile(self, name: str, size: int)->FileSystemInterface:
        file = File(name, size)
        return file

    def appendInFolder(self, folder: FileSystemInterface, item: FileSystemInterface):
        if isinstance(folder, Folder):
            folder.add(item)
        else:
            print('Cannot add item to a file: ', folder.getName())

    def ls(self, item: FileSystemInterface):
        item.ls()

    def openAll(self, item: FileSystemInterface):
        item.openAll()

    def cd(self, item: FileSystemInterface, target: str):
        return item.cd(target)

    def getSize(self, item: FileSystemInterface):
        print(item.getSize())

    def getName(self, item: FileSystemInterface):
        print(item.getName())
        