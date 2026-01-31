from notifier.Iobserver import IObserver

class ConsoleNotifier(IObserver):

    def __init__(self):
        super().__init__()


    def update(self, msg: str):
        print(msg)