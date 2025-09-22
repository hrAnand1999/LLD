from vehicleInterface import VehicleInterface

class Bike(VehicleInterface):

    def __init__(self):
        super().__init__()

    def drive(self):
        print(f'Bike is driving')