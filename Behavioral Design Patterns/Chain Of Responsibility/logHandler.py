from abc import abstractmethod

class LogHandler:

    def __init__(self, handler):
        self.nextHandler = handler

    # def setNextHandler(self, handler):
    #     self.nextHandler = handler

    def handle(self, request):
        if self.nextHandler != None:
            return self.nextHandler.handle(request)
        else:
            print("Unknown Handler")