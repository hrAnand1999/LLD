from vehicleInterface import VehicleInterface

class Car(VehicleInterface):

    def __init__(self):
        super().__init__()

    def drive(self):
        print(f'Car is driving')