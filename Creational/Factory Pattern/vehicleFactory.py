from car import Car
from bike import Bike
from cycle import Cycle

class Vehicle:

    def __init__(self):
        pass

    def getVehicle(self, type):
        if type == 'CAR':
            return Car()
        elif type == 'BIKE':
            return Bike()
        elif type == 'CYCLE':
            return Cycle()
        else:
            return None
        
