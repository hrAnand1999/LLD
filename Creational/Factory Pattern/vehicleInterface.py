from abc import abstractmethod

class VehicleInterface:

    def __init__(self):
        pass

    @abstractmethod
    def drive(self):
        pass