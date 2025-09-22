from logHandler import LogHandler

class Info(LogHandler):

    def __init__(self, handler):
        self.nextHandler = handler

    def handle(self, request):
        if request == 'INFO':
            print("Handling info request")
        elif self.nextHandler != None:
            return self.nextHandler.handle(request)
        else:
            print("Unknown Handler")