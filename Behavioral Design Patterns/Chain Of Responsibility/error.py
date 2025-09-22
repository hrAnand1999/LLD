from logHandler import LogHandler

class Error(LogHandler):

    def __init__(self, handler):
        self.nextHandler = handler

    def handle(self, request):
        if request == 'ERROR':
            print("Handling error request")
        elif self.nextHandler != None:
            return self.nextHandler.handle(request)
        else:
            print("Unknown Handler")