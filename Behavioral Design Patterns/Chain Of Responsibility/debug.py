from logHandler import LogHandler

class Debug(LogHandler):

    def __init__(self, handler):
        self.nextHandler = handler

    def handle(self, request):
        if request == 'DEBUG':
            print("Handling debug request")
        elif self.nextHandler != None:
            return self.nextHandler.handle(request)
        else:
            print("Unknown Handler")