from observerInterface import ObserverInterface

class Observer(ObserverInterface):

    def __init__(self, name):
        self.name = name

    def update(self, observable):
        print(f'{observable.getData()}')
        print(f'{self.name} has been notified.')