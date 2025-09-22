from info import Info
from debug import Debug
from error import Error
from logHandler import LogHandler

def main():
    logProcessor = LogHandler(Info(Debug(Error(None))))
    # infoHandler = Info()
    # debugHandler = Debug()
    # errorHandler =  Error()

    # logProcessor.setNextHandler(infoHandler)
    # infoHandler.setNextHandler(debugHandler)
    # debugHandler.setNextHandler(errorHandler)

    logProcessor.handle("DEBUG")
    logProcessor.handle("ERROR")
    logProcessor.handle("INFO")
    logProcessor.handle("XYZ")

if __name__ == "__main__":
    main()