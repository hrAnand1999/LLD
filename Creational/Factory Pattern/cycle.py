from vehicleInterface import VehicleInterface

class Cycle(VehicleInterface):

    def __init__(self):
        super().__init__()

    def drive(self):
        print(f'Cycle is driving')