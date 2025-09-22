from abc import ABC, abstractmethod

class IParkingLot(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def park_vehicle(self, vehicle):
        pass

    @classmethod
    def getParkingLot(cls):
        pass


class ParkingLot(IParkingLot):
    _instance = None

    def __init__(self, capacity):
        self.capacity = capacity
        print(f"Parking lot created with capacity: {self.capacity}")

    @classmethod
    def getParkingLot(cls, capacity):
        if cls._instance is None:
            cls._instance = cls(capacity)
        return cls._instance

    def park_vehicle(self, vehicle):
        print(f"Parking vehicle: {vehicle}")

    def getCapacity(self):
        return self.capacity


def main():
    parking_lot1 = ParkingLot.getParkingLot(100)
    parking_lot2 = ParkingLot.getParkingLot(200)

    print(f"Parking Lot 1 Capacity: {parking_lot1.capacity}")
    print(f"Parking Lot 2 Capacity: {parking_lot2.capacity}")

    parking_lot1.park_vehicle("Car A")
    parking_lot2.park_vehicle("Car B")

    print(parking_lot1.getCapacity())
    print(parking_lot2.getCapacity())

    print(f"Are both parking lot instances the same? {parking_lot1 is parking_lot2}")


if __name__ == "__main__":
    main()
