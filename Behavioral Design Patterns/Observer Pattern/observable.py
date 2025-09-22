from observableInterface import ObservableInterface

class Observable(ObservableInterface):
    
    def __init__(self):
        self.listOfSubscribers = []
        self.data = None
        pass

    def addObserver(self, observer):
        if observer not in self.listOfSubscribers:
            self.listOfSubscribers.append(observer)

    def removeObserver(self, observer):
        if observer in self.listOfSubscribers:
            self.listOfSubscribers.remove(observer)

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
        self.notify()  # Notify observers when data changes

    def notify(self):
        for observer in self.listOfSubscribers:
            observer.update(self)