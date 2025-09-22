from abc import ABC, abstractmethod

class FileSystemInterface:

    def __init__(self):
        pass

    @abstractmethod
    def ls(self):
        pass

    @abstractmethod
    def openAll(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def cd(self):
        pass

    @abstractmethod
    def isFolder(self)-> bool:
        pass